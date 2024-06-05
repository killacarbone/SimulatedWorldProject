# world.py
from simulation.element import load_periodic_table, load_element_ratios

class World:
    def __init__(self):
        self.elements = load_periodic_table()
        self.element_ratios = load_element_ratios()
        self.compounds = {}
        self.initialize_elements()

    def initialize_elements(self):
        for symbol, count in self.element_ratios.items():
            for _ in range(count):
                element = next(e for e in self.elements if e.symbol == symbol)
                self.elements.append(element)

    def load_key_compounds(self):
        with open('Data/key_compounds.json', 'r') as file:
            self.key_compounds = json.load(file)

    def time_step(self, step=1.0):
        # Simulate time step
        pass

    def reset(self):
        self.elements = load_periodic_table()
        self.compounds = {}

