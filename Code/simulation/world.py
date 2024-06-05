# world.py
import json
from simulation.element import Element

def load_periodic_table():
    with open('Data/periodic_table.json', 'r') as file:
        periodic_table_data = json.load(file)
    return [Element(**element) for element in periodic_table_data['elements']]

def load_element_ratios():
    with open('Data/element_ratios.json', 'r') as file:
        return json.load(file)['ratios']

class World:
    def __init__(self):
        self.elements = load_periodic_table()
        self.element_ratios = load_element_ratios()
        self.compounds = {}
        self.initialize_elements()
        self.load_key_compounds()

    def initialize_elements(self):
        for symbol, count in self.element_ratios.items():
            for _ in range(count):
                element = next(e for e in self.elements if e.symbol == symbol)
                self.elements.append(element)

    def load_key_compounds(self):
        with open('Data/key_compounds.json', 'r') as file:
            self.key_compounds = json.load(file)

    def time_step(self, step=1.0):
        pass

    def reset(self):
        self.elements = load_periodic_table()
        self.compounds = {}
