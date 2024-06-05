import tkinter as tk
from tkinter import ttk
import threading
import time
from simulation.world import World

class SimulationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulated World Project")

        self.world = World()
        self.running = False
        self.filter_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.start_button = ttk.Button(self.master, text="Start", command=self.start_simulation)
        self.start_button.grid(row=0, column=0, padx=10, pady=10)

        self.pause_button = ttk.Button(self.master, text="Pause", command=self.pause_simulation)
        self.pause_button.grid(row=1, column=0, padx=10, pady=10)

        self.resume_button = ttk.Button(self.master, text="Resume", command=self.resume_simulation)
        self.resume_button.grid(row=2, column=0, padx=10, pady=10)

        self.reset_button = ttk.Button(self.master, text="Reset", command=self.reset_simulation)
        self.reset_button.grid(row=3, column=0, padx=10, pady=10)

        self.filter_entry = ttk.Entry(self.master, textvariable=self.filter_var)
        self.filter_entry.grid(row=0, column=1, padx=10, pady=10)

        self.data_text = tk.Text(self.master, wrap=tk.WORD, height=20, width=80)
        self.data_text.grid(row=1, column=1, rowspan=10, padx=10, pady=10)

        self.status_label = ttk.Label(self.master, text="Status: Ready")
        self.status_label.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

    def start_simulation(self):
        self.running = True
        self.status_label.config(text="Status: Running")
        self.simulation_thread = threading.Thread(target=self.run_simulation)
        self.simulation_thread.start()

    def pause_simulation(self):
        self.running = False
        self.status_label.config(text="Status: Paused")

    def resume_simulation(self):
        self.running = True
        self.status_label.config(text="Status: Running")
        self.simulation_thread = threading.Thread(target=self.run_simulation)
        self.simulation_thread.start()

    def reset_simulation(self):
        self.running = False
        self.world = World()
        self.update_data_display()
        self.status_label.config(text="Status: Reset")

    def run_simulation(self):
        step = 0
        while self.running:
            self.world.time_step(step)
            self.update_data_display()
            step += 1
            time.sleep(1)

    def update_data_display(self, event=None):
        self.data_text.delete(1.0, tk.END)
        data = self.get_simulation_data()
        self.data_text.insert(tk.END, data)

    def get_simulation_data(self):
        filter_symbol = self.filter_var.get()
        elements_data = [
            f"{e.name} ({e.symbol}): Position ({e.position_x}, {e.position_y}), State ({e.state}), Temperature ({e.temperature})"
            for e in self.world.elements if not filter_symbol or e.symbol == filter_symbol
        ]
        compounds_data = "\n".join([f"{compound}: {count}" for compound, count in self.world.compounds.items()])
        return f"Elements:\n" + "\n".join(elements_data) + f"\n\nCompounds:\n{compounds_data}"

    def on_closing(self):
        self.running = False
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimulationApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
