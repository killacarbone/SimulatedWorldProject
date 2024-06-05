import tkinter as tk
from tkinter import ttk
from simulation.world import World

class SimulationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulated World Project")

        self.world = World()
        self.running = False

        self.start_button = ttk.Button(master, text="Start", command=self.start_simulation)
        self.start_button.pack()

        self.pause_button = ttk.Button(master, text="Pause", command=self.pause_simulation)
        self.pause_button.pack()

        self.resume_button = ttk.Button(master, text="Resume", command=self.resume_simulation)
        self.resume_button.pack()

        self.reset_button = ttk.Button(master, text="Reset", command=self.reset_simulation)
        self.reset_button.pack()

        self.filter_var = tk.StringVar()
        self.filter_entry = ttk.Entry(master, textvariable=self.filter_var)
        self.filter_entry.pack()

        self.data_text = tk.Text(master, wrap=tk.WORD)
        self.data_text.pack(expand=True, fill=tk.BOTH)

        self.status_var = tk.StringVar(value="Status: Stopped")
        self.status_label = ttk.Label(master, textvariable=self.status_var)
        self.status_label.pack()

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def start_simulation(self):
        if not self.running:
            self.running = True
            self.status_var.set("Status: Running")
            self.run_simulation()

    def pause_simulation(self):
        if self.running:
            self.running = False
            self.status_var.set("Status: Paused")

    def resume_simulation(self):
        if not self.running:
            self.running = True
            self.status_var.set("Status: Running")
            self.run_simulation()

    def reset_simulation(self):
        self.world = World()
        self.update_data_display()
        self.status_var.set("Status: Reset")

    def run_simulation(self):
        def simulate():
            step = 0
            while self.running:
                self.world.time_step(step)
                step += 1
                self.update_data_display()
                self.master.after(1000, simulate)

        self.master.after(1000, simulate)

    def update_data_display(self):
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
        return "Elements:\n" + "\n".join(elements_data) + f"\n\nCompounds:\n{compounds_data}"

    def on_closing(self):
        self.running = False
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimulationApp(root)
    root.mainloop()
