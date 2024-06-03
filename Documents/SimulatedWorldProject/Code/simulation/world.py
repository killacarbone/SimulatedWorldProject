import json
import random
from .element import Element
from .element_ratios import get_element_ratios
from .key_compounds import get_key_compounds

class World:
    def __init__(self):
        self.elements = []
        self.compounds = []
        self.load_key_compounds()
        self.initialize_elements()

    def add_element(self, element):
        self.elements.append(element)

    def time_step(self, step):
        # Add logic for compound formation with respect to ratios
        for element1 in self.elements:
            for element2 in self.elements:
                if element1 != element2:
                    # Simplified interaction logic for demonstration
                    if element1.reactivity == "high" and element2.reactivity == "high" and random.random() > 0.5:
                        compound_name = f"{element1.symbol}{element2.symbol}"
                        self.compounds.append(compound_name)
                        self.log_compound_formation(compound_name, step)
                    elif element1.reactivity == "moderate" and element2.reactivity == "moderate" and random.random() > 0.8:
                        compound_name = f"{element1.symbol}{element2.symbol}"
                        self.compounds.append(compound_name)
                        self.log_compound_formation(compound_name, step)
                    elif element1.reactivity == "low" and element2.reactivity == "low" and random.random() > 0.95:
                        compound_name = f"{element1.symbol}{element2.symbol}"
                        self.compounds.append(compound_name)
                        self.log_compound_formation(compound_name, step)

    def save_state(self):
        state = {
            "elements": [(e.name, e.symbol, e.atomic_number, e.reactivity, e.stability, e.position_x, e.position_y) for e in self.elements],
            "compounds": self.compounds
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
            self.compounds = state["compounds"]
            print("Previous state loaded successfully.")
        except FileNotFoundError:
            print("No previous state found. Initializing with new elements.")

    def load_key_compounds(self):
        key_compounds = get_key_compounds()
        for name, elements in key_compounds:
            self.compounds.append(name)

    def initialize_elements(self):
        element_ratios = get_element_ratios()
        for symbol, count in element_ratios.items():
            for _ in range(count):
                self.add_element(Element(name=symbol, symbol=symbol, atomic_number=1, reactivity="high", stability="low"))

    def log_compound_formation(self, compound_name, step):
        with open("simulation.log", "a") as log_file:
            log_file.write(f"Step {step}: {compound_name} compound formed\n")
