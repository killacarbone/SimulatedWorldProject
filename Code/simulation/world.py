import json
from simulation.element import Element  # Ensure correct import path

class World:
    def __init__(self):
        self.elements = self.load_periodic_table()
        self.element_ratios = self.load_element_ratios()
        self.key_compounds = self.load_key_compounds()
        self.compounds = {}  # Initialize compounds
        self.initialize_elements()

    def initialize_elements(self):
        for symbol, count in self.element_ratios.items():
            for _ in range(int(count)):  # Fixed issue with float
                element = next((e for e in self.elements if e.symbol == symbol), None)
                if element:
                    self.elements.append(element)

    def load_periodic_table(self):
        with open('Data/periodic_table.json', 'r') as file:
            periodic_table_data = json.load(file)
        return [Element(**element) for element in periodic_table_data['elements']]

    def load_element_ratios(self):
        with open('Data/element_ratios.json', 'r') as file:
            return json.load(file)['ratios']

    def load_key_compounds(self):
        with open('Data/key_compounds.json', 'r') as file:
            self.key_compounds = json.load(file)
    
    def reset(self):
        self.elements = self.load_periodic_table()
        self.element_ratios = self.load_element_ratios()
        self.key_compounds = self.load_key_compounds()
        self.initialize_elements()
        self.compounds = {}  # Reset compounds
    
    def time_step(self, step=1.0):
        # Logic for simulating time step
        pass
