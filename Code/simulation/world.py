import random
from simulation.element import Element

class World:
    def __init__(self):
        self.elements = []
        self.compounds = {}
        self.load_key_compounds()
        self.initialize_elements()

    def time_step(self, step=0.1):
        for element in self.elements:
            element.position_x += random.uniform(-1, 1) * step
            element.position_y += random.uniform(-1, 1) * step
        self.apply_physics()

    def apply_physics(self):
        pass

    def reset(self):
        self.elements = []
        self.compounds = {}
        self.initialize_elements()

    def load_key_compounds(self):
        key_compounds = get_key_compounds()
        self.compounds = key_compounds

    def initialize_elements(self):
        element_ratios = get_element_ratios()
        periodic_table = get_periodic_table()
        for symbol, count in element_ratios.items():
            for _ in range(count):
                element = next((e for e in periodic_table if e.symbol == symbol), None)
                if element:
                    new_element = Element(symbol=element.symbol, name=element.name)
                    new_element.position_x = random.uniform(-100, 100)
                    new_element.position_y = random.uniform(-100, 100)
                    self.add_element(new_element)
                else:
                    print(f"Element {symbol} not found in periodic table.")

    def add_element(self, element):
        self.elements.append(element)
