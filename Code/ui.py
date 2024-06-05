import tkinter as tk
from tkinter import ttk
from simulation.world import World
import threading
import time

class SimulationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulated World Project")

        # Simulation world instance
        self.world = World()

        # UI elements
        self.start_button = tk.Button(master, text="Start", command=self.start_simulation)
        self.start_button.grid(row=0, column=0, padx=5, pady=5)

        self.pause_button = tk.Button(master, text="Pause", command=self.pause_simulation)
        self.pause_button.grid(row=1, column=0, padx=5, pady=5)

        self.resume_button = tk.Button(master, text="Resume", command=self.resume_simulation)
        self.resume_button.grid(row=2, column=0, padx=5, pady=5)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_simulation)
        self.reset_button.grid(row=3, column=0, padx=5, pady=5)

        self.status_label = tk.Label(master, text="Status: Stopped")
        self.status_label.grid(row=4, column=0, padx=5, pady=5)

        self.filter_var = tk.StringVar()
        self.filter_label = tk.Label(master, text="Filter Elements:")
        self.filter_label.grid(row=0, column=1, padx=5, pady=5)
        self.filter_combobox = ttk.Combobox(master, textvariable=self.filter_var)
        self.filter_combobox['values'] = self.get_element_symbols()
        self.filter_combobox.grid(row=0, column=2, padx=5, pady=5)
        self.filter_combobox.bind("<<ComboboxSelected>>", self.update_data_display)

        self.data_text = tk.Text(master, wrap=tk.NONE)
        self.data_text.grid(row=1, column=1, columnspan=2, rowspan=4, sticky='nsew')

        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(1, weight=1)

        self.running = False

    def get_element_symbols(self):
        return sorted(set(e.symbol for e in self.world.elements))

    def start_simulation(self):
        if not self.running:
            self.running = True
            self.simulation_thread = threading.Thread(target=self.run_simulation)
            self.simulation_thread.start()
            self.status_label.config(text="Status: Running")

    def pause_simulation(self):
        self.running = False
        self.status_label.config(text="Status: Paused")

    def resume_simulation(self):
        if not self.running:
            self.running = True
            self.simulation_thread = threading.Thread(target=self.run_simulation)
            self.simulation_thread.start()
            self.status_label.config(text="Status: Running")

    def reset_simulation(self):
        self.running = False
        self.world = World()  # Reset the world
        self.update_data_display()
        self.status_label.config(text="Status: Reset")

    def run_simulation(self):
        step = 0
        while self.running:
            if not self.running:
                break
            self.world.time_step(step)
            self.update_data_display()
            step += 1
            time.sleep(1)  # Adjust the speed of simulation as needed
        self.master.after(0, lambda: self.status_label.config(text="Status: Stopped"))  # Ensure update runs in main thread

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
