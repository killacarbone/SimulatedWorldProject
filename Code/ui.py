import tkinter as tk
from tkinter import ttk
from simulation.world import World

class SimulationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulated World Project")

        # Create a frame to hold the buttons and status label
        control_frame = tk.Frame(self.master)
        control_frame.grid(row=0, column=0, sticky="nw")

        self.start_button = tk.Button(control_frame, text="Start", command=self.start_simulation)
        self.start_button.grid(row=0, column=0, padx=10, pady=5)

        self.pause_button = tk.Button(control_frame, text="Pause", command=self.pause_simulation)
        self.pause_button.grid(row=1, column=0, padx=10, pady=5)

        self.resume_button = tk.Button(control_frame, text="Resume", command=self.resume_simulation)
        self.resume_button.grid(row=2, column=0, padx=10, pady=5)

        self.reset_button = tk.Button(control_frame, text="Reset", command=self.reset_simulation)
        self.reset_button.grid(row=3, column=0, padx=10, pady=5)

        self.status_label = tk.Label(control_frame, text="Status: Stopped")
        self.status_label.grid(row=4, column=0, padx=10, pady=5)

        self.filter_var = tk.StringVar()
        self.filter_var.set("")
        self.filter_entry = ttk.Combobox(control_frame, textvariable=self.filter_var)
        self.filter_entry.grid(row=5, column=0, padx=10, pady=5)
        self.filter_entry.bind('<<ComboboxSelected>>', self.update_data_display)

        # Create a frame to hold the data display
        self.data_frame = tk.Frame(self.master)
        self.data_frame.grid(row=0, column=1, sticky="nsew")

        self.data_text = tk.Text(self.data_frame, wrap="word")
        self.data_text.grid(row=0, column=0, sticky="nsew")

        # Configure column and row weights for scaling
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(0, weight=1)
        self.data_frame.grid_columnconfigure(0, weight=1)
        self.data_frame.grid_rowconfigure(0, weight=1)

        self.world = World()
        self.update_filter_options()

    def update_filter_options(self):
        element_symbols = sorted(set(e.symbol for e in self.world.elements))
        self.filter_entry['values'] = element_symbols

    def update_data_display(self, event=None):
        self.data_text.delete(1.0, tk.END)
        self.data_text.insert(tk.END, self.get_simulation_data())

    def get_simulation_data(self):
        filter_symbol = self.filter_var.get()
        elements_data = [
            f"{e.name} ({e.symbol}): Position ({e.position_x}, {e.position_y}), State ({e.state}), Temperature ({e.temperature})"
            for e in self.world.elements if not filter_symbol or e.symbol == filter_symbol
        ]
        compounds_data = "\n".join([f"{compound}: {count}" for compound, count in self.world.compounds.items()])
        return f"Elements:\n" + "\n".join(elements_data) + f"\n\nCompounds:\n{compounds_data}"

    def start_simulation(self):
        self.status_label.config(text="Status: Running")
        self.world = World()  # Reinitialize the world
        self.run_simulation()

    def run_simulation(self):
        self.world.time_step(step=1)  # Pass a default step value
        self.update_data_display()
        self.master.after(1000, self.run_simulation)

    def pause_simulation(self):
        self.status_label.config(text="Status: Paused")

    def resume_simulation(self):
        self.status_label.config(text="Status: Running")
        self.run_simulation()

    def reset_simulation(self):
        self.status_label.config(text="Status: Reset")
        self.world = World()
        self.update_data_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimulationApp(root)
    root.mainloop()
