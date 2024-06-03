# world.py
from random import choice

class World:
    def __init__(self):
        self.elements = []
        self.compounds = []
    
    def add_element(self, element):
        self.elements.append(element)
    
    def combine_elements(self):
        # Define possible combinations and reactions
        possible_combinations = [
            ("H", "O", "Water", "H2O"),
            ("C", "O", "Carbon Dioxide", "CO2"),
            ("N", "H", "Ammonia", "NH3"),
            ("C", "H", "Methane", "CH4"),
            ("S", "O", "Sulfur Dioxide", "SO2")
        ]
        
        for combo in possible_combinations:
            if all(any(e.symbol == elem for e in self.elements) for elem in combo[:2]):
                compound = f"{combo[2]} ({combo[3]}) composed of {' + '.join(combo[:2])}"
                self.compounds.append(compound)
    
    def random_event(self):
        events = ["increase reactivity", "decrease stability"]
        affected_element = choice(self.elements)
        event = choice(events)
        
        if event == "increase reactivity":
            affected_element.reactivity = "very high"
        elif event == "decrease stability":
            affected_element.stability = "very low"
        
        print(f"Random event: {affected_element.name} is affected by {event}")
    
    def __str__(self):
        elements_str = ', '.join(str(e) for e in self.elements)
        compounds_str = ', '.join(self.compounds)
        return f"World with elements: [{elements_str}] and compounds: [{compounds_str}]"
