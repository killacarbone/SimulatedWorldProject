import json
import random
from collections import defaultdict
from .element import Element
from .element_ratios import get_element_ratios
from .key_compounds import get_key_compounds
from .periodic_table import get_periodic_table

class World:
    def __init__(self):
        self.elements = []
        self.compounds = defaultdict(int)
        self.load_key_compounds()
        self.initialize_elements()

    def add_element(self, element):
        self.elements.append(element)

    def time_step(self, step):
        for element1 in self.elements:
            for element2 in self.elements:
                if element1 != element2:
                    if element1.reactivity == "high" and element2.reactivity == "high" and random.random() > 0.5:
                        compound_name = f"{element1.symbol}{element2.symbol}"
                        self.compounds[compound_name] += 1
                    elif element1.reactivity == "moderate" and element2.reactivity == "moderate" and random.random() > 0.8:
                        compound_name = f"{element1.symbol}{element2.symbol}"
                        self.compounds[compound_name] += 1
                    elif element1.reactivity == "low" and element2.reactivity == "low" and random.random() > 0.95:
                        compound_name = f"{element1.symbol}{element2.symbol}"
                        self.compounds[compound_name] += 1

    def save_state(self):
        state = {
            "elements": [(e.name, e.symbol, e.atomic_number, e.reactivity, e.stability, e.mass, e.volume, e.position_x, e.position_y) for e in self.elements],
            "compounds": dict(self.compounds)
        }
        with open("simulation_state.json", "w") as file:
            json.dump(state, file)
        with open("world_state.json", "w") as file:
            json.dump(state, file)
        print("State saved successfully.")

    def load_state(self):
        try:
            with open("simulation_state.json", "r") as file:
                state = json.load(file)
            self.elements = [Element(*e) for e in state["elements"]]
            self.compounds = defaultdict(int, state["compounds"])
            print("Previous state loaded successfully.")
        except FileNotFoundError:
            print("No previous state found. Initializing with new elements.")

    def load_key_compounds(self):
        key_compounds = get_key_compounds()
        for name, elements in key_compounds:
            self.compounds[name] += 1

    def initialize_elements(self):
        element_ratios = get_element_ratios()
        periodic_table = get_periodic_table()
        for symbol, count in element_ratios.items():
            for _ in range(count):
                element = next(e for e in periodic_table if e.symbol == symbol)
                self.add_element(element)
