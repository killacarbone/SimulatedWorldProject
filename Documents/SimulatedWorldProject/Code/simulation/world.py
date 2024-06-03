import random
from .element import Element

class World:
    def __init__(self):
        self.elements = []
        self.compounds = []

    def add_element(self, element: Element):
        self.elements.append(element)

    def form_compound(self, element1: Element, element2: Element):
        compound = f"{element1.symbol}{element2.symbol}"
        self.compounds.append(compound)
        print(f"{compound} compound formed")

    def trigger_random_event(self):
        if not self.elements:
            return

        random_element = random.choice(self.elements)
        event_type = random.choice(["increase reactivity", "decrease stability"])

        if event_type == "increase reactivity":
            random_element.reactivity = "very high"
            print(f"{random_element.name} is affected by {event_type}")
        elif event_type == "decrease stability":
            random_element.stability = "low"
            print(f"{random_element.name} is affected by {event_type}")

    def print_summary(self):
        print("\nWorld Summary:\n")
        print("Elements:")
        for element in self.elements:
            print(f"{element.name} ({element.symbol}), Atomic Number: {element.atomic_number}, Reactivity: {element.reactivity}, Stability: {element.stability}")

        print("\nCompounds:")
        for compound in self.compounds:
            print(compound)

        print("\nRecent Events:")
        for element in self.elements:
            if element.reactivity == "very high":
                print(f"{element.name} is affected by increased reactivity")
            elif element.stability == "low":
                print(f"{element.name} is affected by decreased stability")

class Element:
    def __init__(self, name, symbol, atomic_number, reactivity, stability):
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.reactivity = reactivity
        self.stability = stability

    def __str__(self):
        return f"{self.name} ({self.symbol}), Atomic Number: {self.atomic_number}, Reactivity: {self.reactivity}, Stability: {self.stability}"
