class Compound:
    def __init__(self, name, elements):
        self.name = name
        self.elements = elements

    def __str__(self):
        element_symbols = "".join([element.symbol for element in self.elements])
        return f"{self.name} composed of {element_symbols}"
