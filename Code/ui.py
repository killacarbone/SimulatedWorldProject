import tkinter as tk
from simulation.world import World
import time

class SimulationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulated World Project")
        self.simulation = World()
        self.running = False

        self.start_button = tk.Button(master, text="Start", command=self.start_simulation)
        self.start_button.pack()

        self.pause_button = tk.Button(master, text="Pause", command=self.pause_simulation)
        self.pause_button.pack()

        self.resume_button = tk.Button(master, text="Resume", command=self.resume_simulation)
        self.resume_button.pack()

        self.status_label = tk.Label(master, text="Status: Paused")
        self.status_label.pack()

        self.data_text = tk.Text(master)
        self.data_text.pack()

    def start_simulation(self):
        self.running = True
        self.status_label.config(text="Status: Running")
        self.run_simulation()

    def pause_simulation(self):
        self.running = False
        self.status_label.config(text="Status: Paused")

    def resume_simulation(self):
        self.running = True
        self.status_label.config(text="Status: Running")
        self.run_simulation()

    def run_simulation(self):
        step = 0
        while self.running:
            if not self.running:
                self.status_label.config(text="Status: Paused")
                break

            self.simulation.time_step(step)
            self.update_data_display()
            step += 1
            time.sleep(1)  # Adjust the speed of simulation as needed

        self.status_label.config(text="Status: Stopped")

    def update_data_display(self):
        self.data_text.delete(1.0, tk.END)
        data = self.get_simulation_data()
        self.data_text.insert(tk.END, data)

    def get_simulation_data(self):
        elements_data = "\n".join([f"{e.name} ({e.symbol}): Position ({e.position_x}, {e.position_y}), State {e.state}, Temperature {e.temperature}" for e in self.simulation.elements])
        compounds_data = "\n".join([f"{compound}: {count}" for compound, count in self.simulation.compounds.items()])
        return f"Elements:\n{elements_data}\n\nCompounds:\n{compounds_data}"

    def on_closing(self):
        self.running = False
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimulationApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
