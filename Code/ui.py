import tkinter as tk
from tkinter import ttk
import threading
from simulation.world import World
import time

class SimulationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulated World Project")
        
        self.simulation = World()
        self.running = False
        
        self.create_widgets()
        self.update_status("Paused")
    
    def create_widgets(self):
        self.start_button = ttk.Button(self.master, text="Start", command=self.start_simulation)
        self.start_button.pack()
        
        self.pause_button = ttk.Button(self.master, text="Pause", command=self.pause_simulation)
        self.pause_button.pack()
        
        self.resume_button = ttk.Button(self.master, text="Resume", command=self.resume_simulation)
        self.resume_button.pack()
        
        self.status_label = ttk.Label(self.master, text="Status: Paused")
        self.status_label.pack()
        
        self.data_text = tk.Text(self.master, height=20, width=100)
        self.data_text.pack()

    def start_simulation(self):
        if not self.running:
            self.running = True
            self.simulation_thread = threading.Thread(target=self.run_simulation)
            self.simulation_thread.start()
            self.update_status("Running")

    def pause_simulation(self):
        self.running = False
        self.update_status("Paused")
    
    def resume_simulation(self):
        if not self.running:
            self.running = True
            self.simulation_thread = threading.Thread(target=self.run_simulation)
            self.simulation_thread.start()
            self.update_status("Running")

    def run_simulation(self):
        step = 0
        while self.running:
            self.simulation.time_step(step)
            self.update_data_display()
            step += 1
            time.sleep(0.1)  # Adjust the speed of simulation as needed
        self.update_status("Stopped")

    def update_data_display(self):
        self.data_text.delete(1.0, tk.END)
        data = self.get_simulation_data()
        self.data_text.insert(tk.END, data)

    def get_simulation_data(self):
        elements_data = "\n".join([f"{e.name} ({e.symbol}): Position ({e.position_x}, {e.position_y}), State ({e.state}), Temperature ({e.temperature})" for e in self.simulation.elements])
        compounds_data = "\n".join([f"{compound}: {count}" for compound, count in self.simulation.compounds.items()])
        return f"Elements:\n{elements_data}\n\nCompounds:\n{compounds_data}"

    def update_status(self, status):
        self.status_label.config(text=f"Status: {status}")
    
    def on_closing(self):
        self.running = False
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimulationApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
