from simulation.element import Element
import json

class World:
    def __init__(self):
        self.elements = self.load_periodic_table()
        self.element_ratios = self.load_element_ratios()
        self.compounds = {}
        self.initialize_elements()

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

    def initialize_elements(self):
        for symbol, count in self.element_ratios.items():
            for _ in range(int(count)):
                element = next(e for e in self.elements if e.symbol == symbol)
                self.elements.append(element)

    def time_step(self, step=1.0):
        pass
