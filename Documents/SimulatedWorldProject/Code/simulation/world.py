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
