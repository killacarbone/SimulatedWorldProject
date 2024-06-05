import json
from simulation.element import Element

class World:
    def __init__(self):
        self.elements = self.load_periodic_table()
        self.element_ratios = self.load_element_ratios()
        self.compounds = {}
        self.initialize_elements()

    def initialize_elements(self):
        for symbol, count in self.element_ratios.items():
            element = next(e for e in self.elements if e.symbol == symbol)
            self.elements.extend([element] * int(count))  # Ensure count is an integer

    def load_key_compounds(self):
        with open('Data/key_compounds.json', 'r') as file:
            self.key_compounds = json.load(file)

    def time_step(self, step=1.0):
        # Simulate time step
        pass

# Simulate world
world = World()
