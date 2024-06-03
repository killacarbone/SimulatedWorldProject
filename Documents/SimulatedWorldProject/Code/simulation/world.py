import random
from simulation.element import Element

class World:
    def __init__(self):
        self.elements = []
        self.recent_events = []
        self.compounds = []

    def add_element(self, element):
        self.elements.append(element)

    def form_compounds(self):
        # Add logic to form new compounds based on elements present
        possible_combinations = [
            ("H", "O"), ("C", "O"), ("N", "H"), ("C", "H"), ("S", "O"),
            ("H", "N"), ("H", "C"), ("O", "C"), ("N", "O")
        ]
        for combo in possible_combinations:
            elements_in_combo = [e.symbol for e in self.elements]
            if all(e in elements_in_combo for e in combo):
                compound_name = f"{combo[0]}{combo[1]}"
                if compound_name not in self.compounds:
                    self.compounds.append(compound_name)
                    self.recent_events.append(f"{compound_name} compound formed")
                else:
                    self.recent_events.append("No reaction")

    def trigger_random_event(self):
        # Randomly select an element and modify its properties
        if self.elements:
            element = random.choice(self.elements)
            event_type = random.choice(["reactivity", "stability"])
            if event_type == "reactivity":
                element.reactivity = "very high" if element.reactivity == "high" else "high"
                self.recent_events.append(f"{element.name} is affected by increased reactivity")
            elif event_type == "stability":
                element.stability = "low" if element.stability == "high" else "high"
                self.recent_events.append(f"{element.name} is affected by decreased stability")
        self.form_compounds()

    def print_summary(self):
        print("\nWorld Summary:")
        print("Elements:")
        for element in self.elements:
            print(element)
        print("\nCompounds:")
        for compound in self.compounds:
            print(compound)
        print("\nRecent Events:")
        for event in self.recent_events:
            print(event)
        self.recent_events.clear()
