import tkinter as tk
from tkinter import ttk
from simulation.world import World

class SimulationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulated World Project")

        self.world = World()
        self.running = False

        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        self.start_button = tk.Button(self.master, text="Start", command=self.start_simulation)
        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_simulation)
        self.resume_button = tk.Button(self.master, text="Resume", command=self.resume_simulation)
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_simulation)

        self.status_label = tk.Label(self.master, text="Status: Stopped")
        
        self.filter_var = tk.StringVar()
        self.filter_entry = ttk.Combobox(self.master, textvariable=self.filter_var)
        self.filter_entry['values'] = [e.symbol for e in self.world.elements]
        self.filter_entry.bind("<<ComboboxSelected>>", self.update_data_display)

        self.data_text = tk.Text(self.master, wrap=tk.NONE)
        self.data_scroll_x = tk.Scrollbar(self.master, orient=tk.HORIZONTAL, command=self.data_text.xview)
        self.data_scroll_y = tk.Scrollbar(self.master, orient=tk.VERTICAL, command=self.data_text.yview)
        self.data_text.configure(xscrollcommand=self.data_scroll_x.set, yscrollcommand=self.data_scroll_y.set)

    def layout_widgets(self):
        self.start_button.grid(row=0, column=0, padx=5, pady=5)
        self.pause_button.grid(row=1, column=0, padx=5, pady=5)
        self.resume_button.grid(row=2, column=0, padx=5, pady=5)
        self.reset_button.grid(row=3, column=0, padx=5, pady=5)
        
        self.status_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        
        self.filter_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        self.data_text.grid(row=1, column=1, rowspan=4, padx=5, pady=5, sticky="nsew")
        self.data_scroll_x.grid(row=5, column=1, padx=5, pady=5, sticky="ew")
        self.data_scroll_y.grid(row=1, column=2, rowspan=4, padx=5, pady=5, sticky="ns")

        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

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
        self.world = World()
        self.update_data_display()
        self.status_label.config(text="Status: Reset")

    def run_simulation(self):
        if self.running:
            self.world.time_step()
            self.update_data_display()
            self.master.after(1000, self.run_simulation)

    def update_data_display(self, event=None):
        data = self.get_simulation_data()
        self.data_text.config(state=tk.NORMAL)
        self.data_text.delete(1.0, tk.END)
        self.data_text.insert(tk.END, data)
        self.data_text.config(state=tk.DISABLED)

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
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
