import random
from .element import Element

class World:
    def __init__(self):
        self.elements = []
        self.compounds = []
        self.time_step = 0
        self.reactions = []

    def add_element(self, element):
        self.elements.append(element)

    def trigger_random_event(self):
        event = random.choice(self.elements)
        if event.reactivity == "high":
            event.reactivity = "very high"
            print(f"{event.name} is affected by increased reactivity")
        elif event.reactivity == "moderate":
            event.stability = "low"
            print(f"{event.name} is affected by decreased stability")
        self.reactions.append(f"{event.name} is affected by {event.reactivity}")

    def update(self):
        self.time_step += 1
        new_compounds = []
        for i, elem1 in enumerate(self.elements):
            for elem2 in self.elements[i+1:]:
                if elem1.reactivity == "very high" and elem2.reactivity in ["high", "very high"]:
                    compound = f"{elem1.symbol}{elem2.symbol}"
                    if compound not in self.compounds:
                        new_compounds.append(compound)
                        print(f"{compound} compound formed")
        self.compounds.extend(new_compounds)

    def print_summary(self):
        print(f"Time step: {self.time_step}\n")
        print("World Summary:")
        print("Elements:")
        for element in self.elements:
            print(element)
        print("\nCompounds:")
        for compound in self.compounds:
            print(compound)
        print("\nRecent Events:")
        for reaction in self.reactions:
            print(reaction)

