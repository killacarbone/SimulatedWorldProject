import json
from simulation.element import Element

class World:
    def __init__(self):
        self.elements = []
        self.compounds = {}
        self.load_key_compounds()
        self.load_elements()
        self.initialize_elements()

    def load_key_compounds(self):
        with open('Data/key_compounds.json', 'r') as file:
            self.key_compounds = json.load(file)['key_compounds']

    def load_elements(self):
        with open('Data/element_ratios.json', 'r') as file:
            self.element_ratios = json.load(file)['ratios']
        with open('Data/periodic_table.json', 'r') as file:
            self.periodic_table_data = json.load(file)['elements']
        self.periodic_table = [Element(**element) for element in self.periodic_table_data]

    def initialize_elements(self):
        for symbol, count in self.element_ratios.items():
            element = next(e for e in self.periodic_table if e.symbol == symbol)
            for _ in range(int(count * 1000)):  # Multiply count for simulation scale
                self.elements.append(element)

    def time_step(self, step=0.1):
        # Simulation logic (e.g., moving elements, forming compounds)
        pass

    def reset(self):
        self.elements = []
        self.compounds = {}
        self.initialize_elements()
