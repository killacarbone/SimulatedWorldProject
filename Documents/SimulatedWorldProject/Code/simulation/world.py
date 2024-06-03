from simulation.element import Element

class Compound:
    def __init__(self, name, components):
        self.name = name
        self.components = components

    def __str__(self):
        component_names = ' + '.join([component.name for component in self.components])
        return f"{self.name} composed of {component_names}"

class World:
    def __init__(self):
        self.elements = []
        self.compounds = []
        self.rules = {
            ("Hydrogen", "Oxygen"): "Water",
            ("Carbon", "Oxygen"): "Carbon Dioxide",
            # Add more rules as needed
        }

    def add_element(self, element):
        self.elements.append(element)

    def combine_elements(self):
        combined_elements = []
        for i, element1 in enumerate(self.elements):
            for element2 in self.elements[i+1:]:
                compound_name = self.rules.get((element1.name, element2.name)) or self.rules.get((element2.name, element1.name))
                if compound_name:
                    compound = Compound(compound_name, [element1, element2])
                    self.compounds.append(compound)
                    combined_elements.append(compound)
        return combined_elements

    def __str__(self):
        elements_str = ', '.join([str(e) for e in self.elements])
        compounds_str = ', '.join([str(c) for c in self.compounds])
        return f"World with elements: [{elements_str}] and compounds: [{compounds_str}]"
