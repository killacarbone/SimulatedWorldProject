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

        self.start_button = tk.Button(master, text="Start", command=self.start_simulation)
        self.start_button.pack()

        self.pause_button = tk.Button(master, text="Pause", command=self.pause_simulation)
        self.pause_button.pack()

        self.resume_button = tk.Button(master, text="Resume", command=self.resume_simulation)
        self.resume_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_simulation)
        self.stop_button.pack()

        self.status_label = tk.Label(master, text="Status: Paused")
        self.status_label.pack()

        self.filter_label = tk.Label(master, text="Filter Elements:")
        self.filter_label.pack()

        self.filter_var = tk.StringVar()
        self.filter_var.set("")
        self.filter_dropdown = ttk.Combobox(master, textvariable=self.filter_var)
        self.filter_dropdown['values'] = self.get_element_symbols()
        self.filter_dropdown.pack()

        self.data_text = tk.Text(master, wrap='word', width=80, height=20)
        self.data_text.pack()

    def start_simulation(self):
        self.running = True
        self.simulation_thread = threading.Thread(target=self.run_simulation)
        self.simulation_thread.start()
        self.status_label.config(text="Status: Running")

    def pause_simulation(self):
        self.running = False
        self.status_label.config(text="Status: Paused")

    def resume_simulation(self):
        self.running = True
        self.simulation_thread = threading.Thread(target=self.run_simulation)
        self.simulation_thread.start()
        self.status_label.config(text="Status: Running")

    def stop_simulation(self):
        self.running = False
        self.world = World()  # Reset world to initial state
        self.status_label.config(text="Status: Stopped")
        self.update_data_display()

    def run_simulation(self):
        step = 0
        while self.running:
            if not self.running:
                break
            self.world.time_step(step)
            self.update_data_display()
            step += 1
            time.sleep(1)  # Adjust the speed of simulation as needed
        self.status_label.config(text="Status: Stopped")

    def update_data_display(self):
        self.data_text.delete(1.0, tk.END)
        data = self.get_simulation_data()
        self.data_text.insert(tk.END, data)

    def get_simulation_data(self):
        filter_symbol = self.filter_var.get()
        elements_data = "\n".join([f"{e.name} ({e.symbol}): Position ({e.position_x}, {e.position_y}), State ({e.state}), Temperature ({e.temperature})"
                                   for e in self.world.elements if not filter_symbol or e.symbol == filter_symbol])
        compounds_data = "\n".join([f"{compound}: {count}" for compound, count in self.world.compounds.items()])
        return f"Elements:\n{elements_data}\n\nCompounds:\n{compounds_data}"

    def get_element_symbols(self):
        return [element.symbol for element in self.world.elements]

if __name__ == "__main__":
    root = tk.Tk()
    app = SimulationApp(root)
    root.mainloop()
