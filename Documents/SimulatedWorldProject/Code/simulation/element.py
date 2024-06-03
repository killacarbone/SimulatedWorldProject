class Element:
    def __init__(self, name, symbol, atomic_number, reactivity, stability, x, y):
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.reactivity = reactivity
        self.stability = stability
        self.x = x  # Position in the 2D space
        self.y = y  # Position in the 2D space

    def __str__(self):
        return f"{self.name} ({self.symbol}), Atomic Number: {self.atomic_number}, Reactivity: {self.reactivity}, Stability: {self.stability}"

# Define the periodic table with more elements
periodic_table = [
    Element("Hydrogen", "H", 1, "high", "low", 0, 0),
    Element("Helium", "He", 2, "low", "high", 0, 0),
    Element("Lithium", "Li", 3, "high", "low", 0, 0),
    Element("Beryllium", "Be", 4, "moderate", "high", 0, 0),
    Element("Boron", "B", 5, "moderate", "high", 0, 0),
    Element("Carbon", "C", 6, "high", "high", 0, 0),
    Element("Nitrogen", "N", 7, "high", "high", 0, 0),
    Element("Oxygen", "O", 8, "very high", "low", 0, 0),
    Element("Fluorine", "F", 9, "very high", "low", 0, 0),
    Element("Neon", "Ne", 10, "low", "high", 0, 0),
    # Add all other elements up to Oganesson (element 118)
    Element("Rhenium", "Re", 75, "moderate", "moderate", 0, 0),
    Element("Osmium", "Os", 76, "moderate", "moderate", 0, 0),
    Element("Iridium", "Ir", 77, "moderate", "stable", 0, 0),
    Element("Platinum", "Pt", 78, "moderate", "high", 0, 0),
    Element("Gold", "Au", 79, "moderate", "stable", 0, 0),
    Element("Mercury", "Hg", 80, "low", "low", 0, 0),
    Element("Thallium", "Tl", 81, "moderate", "low", 0, 0),
    Element("Lead", "Pb", 82, "moderate", "moderate", 0, 0),
    Element("Bismuth", "Bi", 83, "moderate", "moderate", 0, 0),
    Element("Polonium", "Po", 84, "high", "low", 0, 0),
    Element("Astatine", "At", 85, "high", "low", 0, 0),
    Element("Radon", "Rn", 86, "low", "low", 0, 0),
    Element("Francium", "Fr", 87, "very high", "low", 0, 0),
    Element("Radium", "Ra", 88, "high", "low", 0, 0),
    Element("Actinium", "Ac", 89, "moderate", "moderate", 0, 0),
    Element("Thorium", "Th", 90, "moderate", "moderate", 0, 0),
    Element("Protactinium", "Pa", 91, "moderate", "low", 0, 0),
    Element("Uranium", "U", 92, "moderate", "low", 0, 0),
    Element("Neptunium", "Np", 93, "moderate", "low", 0, 0),
    Element("Plutonium", "Pu", 94, "moderate", "low", 0, 0),
    Element("Americium", "Am", 95, "moderate", "low", 0, 0),
    Element("Curium", "Cm", 96, "moderate", "low", 0, 0),
    Element("Berkelium", "Bk", 97, "moderate", "low", 0, 0),
    Element("Californium", "Cf", 98, "moderate", "low", 0, 0),
    Element("Einsteinium", "Es", 99, "moderate", "low", 0, 0),
    Element("Fermium", "Fm", 100, "moderate", "low", 0, 0),
    Element("Mendelevium", "Md", 101, "moderate", "low", 0, 0),
    Element("Nobelium", "No", 102, "moderate", "low", 0, 0),
    Element("Lawrencium", "Lr", 103, "moderate", "low", 0, 0),
    Element("Rutherfordium", "Rf", 104, "moderate", "low", 0, 0),
    Element("Dubnium", "Db", 105, "moderate", "low", 0, 0),
    Element("Seaborgium", "Sg", 106, "moderate", "low", 0, 0),
    Element("Bohrium", "Bh", 107, "high", "low", 0, 0),
    Element("Hassium", "Hs", 108, "high", "low", 0, 0),
    Element("Meitnerium", "Mt", 109, "moderate", "low", 0, 0),
    Element("Darmstadtium", "Ds", 110, "moderate", "low", 0, 0),
    Element("Roentgenium", "Rg", 111, "moderate", "low", 0, 0),
    Element("Copernicium", "Cn", 112, "moderate", "low", 0, 0),
    Element("Nihonium", "Nh", 113, "moderate", "low", 0, 0),
    Element("Flerovium", "Fl", 114, "moderate", "low", 0, 0),
    Element("Moscovium", "Mc", 115, "moderate", "low", 0, 0),
    Element("Livermorium", "Lv", 116, "moderate", "low", 0, 0),
    Element("Tennessine", "Ts", 117, "moderate", "low", 0, 0),
    Element("Oganesson", "Og", 118, "moderate", "low", 0, 0)
]

# Export the periodic table
def get_periodic_table():
    return periodic_table
