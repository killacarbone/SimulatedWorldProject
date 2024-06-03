import random
import math
from simulation.elements import Element, get_periodic_table

class World:
    def __init__(self):
        self.elements = get_periodic_table()
        self.compounds = []
        self.time_step_count = 0
        self.temperature = 25  # Example environmental condition

    def add_element(self, element):
        self.elements.append(element)

    def time_step(self):
        self.time_step_count += 1
        print(f"Time step: {self.time_step_count}")
        self.check_interactions()
        self.random_event()
        self.print_summary()

    def check_interactions(self):
        for element1 in self.elements:
            for element2 in self.elements:
                if element1 != element2 and self.can_form_compound(element1, element2):
                    compound_name = f"{element1.symbol}{element2.symbol}"
                    if compound_name not in self.compounds:
                        self.compounds.append(compound_name)
                        print(f"{compound_name} compound formed")

    def can_form_compound(self, element1, element2):
        distance = math.sqrt((element1.x - element2.x)**2 + (element1.y - element2.y)**2)
        if distance < 10:  # Example proximity condition
            if element1.reactivity == "high" and element2.reactivity == "high" and self.temperature > 20:
                return random.random() > 0.5
            elif element1.reactivity == "moderate" and element2.reactivity == "moderate" and self.temperature > 15:
                return random.random() > 0.8
            elif element1.reactivity == "low" and element2.reactivity == "low" and self.temperature > 10:
                return random.random() > 0.95
        return False

    def random_event(self):
        event_chance = random.random()
        if event_chance > 0.8:
            element = random.choice(self.elements)
            if event_chance > 0.9:
                element.stability = "low"
                print(f"{element.name} is affected by decreased stability")
            else:
                element.reactivity = "high"
                print(f"{element.name} is affected by increased reactivity")

    def print_summary(self):
        print("\nWorld Summary:")
        print("Elements:")
        for element in self.elements:
            print(element)
        print("\nCompounds:")
        for compound in self.compounds:
            print(compound)
        print("\nRecent Events:")
        # Placeholder for events, should be populated during time steps
