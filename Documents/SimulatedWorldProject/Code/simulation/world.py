import random
from simulation.element import Element

class World:
    def __init__(self):
        self.elements = []
        self.compounds = []
        self.time_step_count = 0

    def add_element(self, element):
        self.elements.append(element)

    def time_step(self):
        self.time_step_count += 1
        print(f"Time step: {self.time_step_count}")

        # Check for compound formation with a probability
        for element1 in self.elements:
            for element2 in self.elements:
                if element1 != element2:
                    # Check if elements can form a compound based on reactivity and a random chance
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

    def print_summary(self):
        print("World Summary:")
        print("Elements:")
        for element in self.elements:
            print(element)
        print("\nCompounds:")
        for compound in self.compounds:
            print(compound)
