import random
import json
from simulation.element import Element
from simulation.key_compounds import get_key_compounds
from simulation.element_ratios import get_element_ratios

class World:
    def __init__(self):
        self.elements = []
        self.compounds = []
        self.key_compounds = get_key_compounds()
        self.element_ratios = get_element_ratios()

    def initialize_elements(self, total_elements=1000):
        for symbol, ratio in self.element_ratios.items():
            count = int(total_elements * (ratio / 100))
            for _ in range(count):
                element = Element(name=symbol, symbol=symbol, atomic_number=1, reactivity="high", stability="low", position_x=random.randint(0, 100), position_y=random.randint(0, 100))
                self.add_element(element)

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
        # Check if the pair forms a key compound
        if (element1.symbol, element2.symbol) in self.key_compounds:
            return self.key_compounds[(element1.symbol, element2.symbol)]
        elif (element2.symbol, element1.symbol) in self.key_compounds:
            return self.key_compounds[(element2.symbol, element1.symbol)]
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
