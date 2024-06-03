# world.py
class World:
    def __init__(self):
        self.elements = []
        self.compounds = []
    
    def add_element(self, element):
        self.elements.append(element)
    
    def combine_elements(self):
        # This is a placeholder for a more complex combination logic
        # Example: Water from Hydrogen and Oxygen
        if any(e.symbol == "H" for e in self.elements) and any(e.symbol == "O" for e in self.elements):
            water = f"Water composed of Hydrogen + Oxygen"
            self.compounds.append(water)
        # Example: Carbon Dioxide from Carbon and Oxygen
        if any(e.symbol == "C" for e in self.elements) and any(e.symbol == "O" for e in self.elements):
            carbon_dioxide = f"Carbon Dioxide composed of Oxygen + Carbon"
            self.compounds.append(carbon_dioxide)
    
    def __str__(self):
        elements_str = ', '.join(str(e) for e in self.elements)
        compounds_str = ', '.join(self.compounds)
        return f"World with elements: [{elements_str}] and compounds: [{compounds_str}]"
