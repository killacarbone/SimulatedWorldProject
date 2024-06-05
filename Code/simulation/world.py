import json
from .element import periodic_table, element_ratios

class World:
    def __init__(self):
        self.elements = periodic_table
        self.compounds = {}
        self.load_key_compounds()
        self.initialize_elements()

    def load_key_compounds(self):
        with open('Data/key_compounds.json', 'r') as file:
            self.key_compounds = json.load(file)['key_compounds']

    def initialize_elements(self):
        for symbol, count in element_ratios.items():
            for element in self.elements:
                if element.symbol == symbol:
                    element.count = count
                    break

    def time_step(self, step=0.1):
        # Simulate time step for elements and compounds
        pass

    def reset(self):
        self.compounds = {}
        self.initialize_elements()

# Example usage
world = World()
world.time_step()
