import random
import json
from simulation.element import Element

class World:
    def __init__(self):
        self.elements = []
        self.compounds = []

    def add_element(self, element):
        self.elements.append(element)

    def time_step(self):
        # Check for compound formation with a probability
        for element1 in self.elements:
            for element2 in self.elements:
                if element1 != element2:
                    compound_name = self.form_compound(element1, element2)
                    if compound_name:
                        self.compounds.append(compound_name)
                        print(f"{compound_name} compound formed")

    def form_compound(self, element1, element2):
        # Compound formation logic
        # This will be a basic example and can be extended further
        if (element1.symbol, element2.symbol) in [("H", "O"), ("O", "H")]:
            return "H2O"
        elif (element1.symbol, element2.symbol) in [("H", "H")]:
            return "H2"
        elif (element1.symbol, element2.symbol) in [("O", "O")]:
            return "O2"
        else:
            # Check for random less common compounds
            if element1.reactivity == "high" and element2.reactivity == "high" and random.random() > 0.5:
                return f"{element1.symbol}{element2.symbol}"
            elif element1.reactivity == "moderate" and element2.reactivity == "moderate" and random.random() > 0.8:
                return f"{element1.symbol}{element2.symbol}"
            elif element1.reactivity == "low" and element2.reactivity == "low" and random.random() > 0.95:
                return f"{element1.symbol}{element2.symbol}"
            else:
                return None

    def save_state(self):
        state = {
            "elements": [(e.name, e.symbol, e.atomic_number, e.reactivity, e.stability, e.position_x, e.position_y) for e in self.elements],
            "compounds": self.compounds,
        }
        with open("simulation_state.json", "w") as file:
            json.dump(state, file)

    def load_state(self):
        with open("simulation_state.json", "r") as file:
            state = json.load(file)
            self.elements = [Element(*e) for e in state["elements"]]
            self.compounds = state["compounds"]
