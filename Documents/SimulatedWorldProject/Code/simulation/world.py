class World:
    def __init__(self):
        self.elements = []
        self.compounds = []
        self.events = []

    def add_element(self, element):
        self.elements.append(element)

    def add_compound(self, compound):
        self.compounds.append(compound)

    def add_event(self, event):
        self.events.append(event)

    def simulate_reactions(self):
        for i, element1 in enumerate(self.elements):
            for element2 in self.elements[i + 1:]:
                reaction = element1.react_with(element2)
                if "compound formed" in reaction:
                    self.add_event(reaction)
                    compound_name = reaction.split()[0]
                    if compound_name not in [c for c in self.compounds]:
                        self.add_compound(compound_name)

    def print_summary(self):
        print("World Summary:\n")
        print("Elements:")
        for element in self.elements:
            print(element)
        print("\nCompounds:")
        for compound in self.compounds:
            print(compound)
        print("\nRecent Events:")
        for event in self.events:
            print(event)
