import random
from simulation.element import get_periodic_table

class World:
    def __init__(self):
        self.elements = get_periodic_table()
        self.compounds = []
        self.time_step_count = 0
        self.recent_events = []

    def time_step(self):
        self.time_step_count += 1
        self.recent_events = []
        self.trigger_random_event()
        self.check_for_new_compounds()

    def trigger_random_event(self):
        element = random.choice(self.elements)
        event_type = random.choice(["increase_reactivity", "decrease_reactivity", "increase_stability", "decrease_stability"])
        if event_type == "increase_reactivity":
            self.recent_events.append(f"{element.name} is affected by increased reactivity")
            element.reactivity = "very high"
        elif event_type == "decrease_reactivity":
            self.recent_events.append(f"{element.name} is affected by decreased reactivity")
            element.reactivity = "low"
        elif event_type == "increase_stability":
            self.recent_events.append(f"{element.name} is affected by increased stability")
            element.stability = "high"
        elif event_type == "decrease_stability":
            self.recent_events.append(f"{element.name} is affected by decreased stability")
            element.stability = "low"

    def check_for_new_compounds(self):
        for i in range(len(self.elements)):
            for j in range(i + 1, len(self.elements)):
                element1 = self.elements[i]
                element2 = self.elements[j]
                if random.random() < 0.1:  # Random chance to form a new compound
                    compound = f"{element1.symbol}{element2.symbol}"
                    self.compounds.append(compound)
                    self.recent_events.append(f"{compound} compound formed")

    def print_summary(self):
        print(f"\nTime step: {self.time_step_count}\n")
        print("World Summary:\n")
        print("Elements:")
        for element in self.elements:
            print(element)
        print("\nCompounds:")
        for compound in self.compounds:
            print(compound)
        print("\nRecent Events:")
        for event in self.recent_events:
            print(event)
