import json
import random
from simulation.element import Element

class World:
    def __init__(self):
        self.elements = []
        self.compounds = []
        self.time_step_counter = 0

    def add_element(self, element):
        self.elements.append(element)

    def time_step(self):
        self.time_step_counter += 1
        for element1 in self.elements:
            for element2 in self.elements:
                if element1 != element2:
                    if element1.reactivity == "high" and element2.reactivity == "high" and random.random() > 0.5:
                        compound_name = f"{element1.symbol}{element2.symbol}"
                        self.compounds.append(compound_name)
                        print(f"{compound_name} compound formed")
                    elif element1.reactivity == "moderate" and element2.reactivity == "moderate" and random.random() > 0.8:
                        compound_name = f"{element1.symbol}{element2.symbol}"
                        self.compounds.append(compound_name)
                        print(f"{compound_name} compound formed")
                    elif element1.reactivity == "low" and element2.reactivity == "low" and random.random() > 0.95:
                        compound_name = f"{element1.symbol}{element2.symbol}"
                        self.compounds.append(compound_name)
                        print(f"{compound_name} compound formed")

    def save_state(self):
        state = {
            "elements": [(e.name, e.symbol, e.atomic_number, e.reactivity, e.stability, e.position_x, e.position_y) for e in self.elements],
            "compounds": self.compounds,
            "time_step_counter": self.time_step_counter
        }
        with open('world_state.json', 'w') as f:
            json.dump(state, f)

    def load_state(self):
        with open('world_state.json', 'r') as f:
            state = json.load(f)
        self.elements = [Element(*e) for e in state["elements"]]
        self.compounds = state["compounds"]
        self.time_step_counter = state["time_step_counter"]

    def print_summary(self):
        print(f"\nTime step: {self.time_step_counter}")
        print("\nWorld Summary:")
        print("\nElements:")
        for element in self.elements:
            print(element)
        print("\nCompounds:")
        for compound in self.compounds:
            print(compound)
        print("\nRecent Events:")
        print("No reaction")
