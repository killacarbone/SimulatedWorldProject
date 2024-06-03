class Element:
    def __init__(self, name, symbol, atomic_number, reactivity, stability):
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.reactivity = reactivity
        self.stability = stability

    def __str__(self):
        return f"{self.name} ({self.symbol}), Atomic Number: {self.atomic_number}, Reactivity: {self.reactivity}, Stability: {self.stability}"

# Define the periodic table with more elements
periodic_table = [
    Element("Hydrogen", "H", 1, "high", "low"),
    Element("Helium", "He", 2, "low", "high"),
    Element("Lithium", "Li", 3, "high", "low"),
    Element("Beryllium", "Be", 4, "moderate", "high"),
    Element("Boron", "B", 5, "moderate", "high"),
    Element("Carbon", "C", 6, "high", "high"),
    Element("Nitrogen", "N", 7, "high", "high"),
    Element("Oxygen", "O", 8, "very high", "low"),
    Element("Fluorine", "F", 9, "very high", "low"),
    Element("Neon", "Ne", 10, "low", "high"),
    # Add all other elements up to Oganesson (element 118)
    Element("Rhenium", "Re", 75, "moderate", "moderate"),
    Element("Osmium", "Os", 76, "moderate", "moderate"),
    Element("Iridium", "Ir", 77, "moderate", "stable"),
    Element("Platinum", "Pt", 78, "moderate", "high"),
    Element("Gold", "Au", 79, "moderate", "stable"),
    Element("Mercury", "Hg", 80, "low", "low"),
    Element("Thallium", "Tl", 81, "moderate", "low"),
    Element("Lead", "Pb", 82, "moderate", "moderate"),
    Element("Bismuth", "Bi", 83, "moderate", "moderate"),
    Element("Polonium", "Po", 84, "high", "low"),
    Element("Astatine", "At", 85, "high", "low"),
    Element("Radon", "Rn", 86, "low", "low"),
    Element("Francium", "Fr", 87, "very high", "low"),
    Element("Radium", "Ra", 88, "high", "low"),
    Element("Actinium", "Ac", 89, "moderate", "moderate"),
    Element("Thorium", "Th", 90, "moderate", "moderate"),
    Element("Protactinium", "Pa", 91, "moderate", "low"),
    Element("Uranium", "U", 92, "moderate", "low"),
    Element("Neptunium", "Np", 93, "moderate", "low"),
    Element("Plutonium", "Pu", 94, "moderate", "low"),
    Element("Americium", "Am", 95, "moderate", "low"),
    Element("Curium", "Cm", 96, "moderate", "low"),
    Element("Berkelium", "Bk", 97, "moderate", "low"),
    Element("Californium", "Cf", 98, "moderate", "low"),
    Element("Einsteinium", "Es", 99, "moderate", "low"),
    Element("Fermium", "Fm", 100, "moderate", "low"),
    Element("Mendelevium", "Md", 101, "moderate", "low"),
    Element("Nobelium", "No", 102, "moderate", "low"),
    Element("Lawrencium", "Lr", 103, "moderate", "low"),
    Element("Rutherfordium", "Rf", 104, "moderate", "low"),
    Element("Dubnium", "Db", 105, "moderate", "low"),
    Element("Seaborgium", "Sg", 106, "moderate", "low"),
    Element("Bohrium", "Bh", 107, "high", "low"),
    Element("Hassium", "Hs", 108, "high", "low"),
    Element("Meitnerium", "Mt", 109, "moderate", "low"),
    Element("Darmstadtium", "Ds", 110, "moderate", "low"),
    Element("Roentgenium", "Rg", 111, "moderate", "low"),
    Element("Copernicium", "Cn", 112, "moderate", "low"),
    Element("Nihonium", "Nh", 113, "moderate", "low"),
    Element("Flerovium", "Fl", 114, "moderate", "low"),
    Element("Moscovium", "Mc", 115, "moderate", "low"),
    Element("Livermorium", "Lv", 116, "moderate", "low"),
    Element("Tennessine", "Ts", 117, "moderate", "low"),
    Element("Oganesson", "Og", 118, "moderate", "low")
]

# Export the periodic table
def get_periodic_table():
    return periodic_table
