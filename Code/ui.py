import tkinter as tk
from simulation.world import World

class SimulationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulated World Project")
        self.running = False

        self.create_widgets()
        self.world = World()
        self.update_filter_options()

    def create_widgets(self):
        self.start_button = tk.Button(self.master, text="Start", command=self.start_simulation)
        self.start_button.grid(row=0, column=0, padx=10, pady=5)

        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_simulation)
        self.pause_button.grid(row=1, column=0, padx=10, pady=5)

        self.resume_button = tk.Button(self.master, text="Resume", command=self.resume_simulation)
        self.resume_button.grid(row=2, column=0, padx=10, pady=5)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_simulation)
        self.reset_button.grid(row=3, column=0, padx=10, pady=5)

        self.status_label = tk.Label(self.master, text="Status: Stopped")
        self.status_label.grid(row=4, column=0, padx=10, pady=5)

        self.filter_var = tk.StringVar()
        self.filter_dropdown = tk.OptionMenu(self.master, self.filter_var, '')
        self.filter_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

        self.data_text = tk.Text(self.master, wrap="word", height=20, width=50)
        self.data_text.grid(row=1, column=1, rowspan=4, padx=10, pady=5, sticky='nsew')

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

    def update_filter_options(self):
        element_symbols = sorted(set(e.symbol for e in self.world.elements))
        self.filter_dropdown['menu'].delete(0, 'end')
        for symbol in element_symbols:
            self.filter_dropdown['menu'].add_command(label=symbol, command=tk._setit(self.filter_var, symbol))

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

    def start_simulation(self):
        if not self.running:
            self.running = True
            self.status_label.config(text="Status: Running")
            self.run_simulation()

    def pause_simulation(self):
        self.running = False
        self.status_label.config(text="Status: Paused")

    def resume_simulation(self):
        if not self.running:
            self.running = True
            self.status_label.config(text="Status: Running")
            self.run_simulation()

    def reset_simulation(self):
        self.running = False
        self.status_label.config(text="Status: Reset")
        self.world.reset()
        self.update_data_display()

    def run_simulation(self):
        if self.running:
            self.world.time_step(step=0.1)
            self.update_data_display()
            self.master.after(100, self.run_simulation)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimulationApp(root)
    root.mainloop()
