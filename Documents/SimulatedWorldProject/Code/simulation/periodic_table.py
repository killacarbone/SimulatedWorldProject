class Element:
    def __init__(self, name, symbol, atomic_number, reactivity, stability, mass, volume, position_x=0, position_y=0):
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.reactivity = reactivity
        self.stability = stability
        self.mass = mass
        self.volume = volume
        self.position_x = position_x
        self.position_y = position_y

# Complete periodic table with all elements
periodic_table = [
    Element("Hydrogen", "H", 1, "high", "low", 1.008, 0.08988, 0, 0),
    Element("Helium", "He", 2, "low", "high", 4.0026, 0.1786, 0, 0),
    Element("Lithium", "Li", 3, "high", "low", 6.94, 0.534, 0, 0),
    Element("Beryllium", "Be", 4, "moderate", "high", 9.0122, 1.85, 0, 0),
    Element("Boron", "B", 5, "moderate", "high", 10.81, 2.34, 0, 0),
    Element("Carbon", "C", 6, "high", "high", 12.011, 2.267, 0, 0),
    Element("Nitrogen", "N", 7, "high", "high", 14.007, 1.251, 0, 0),
    Element("Oxygen", "O", 8, "high", "low", 15.999, 1.429, 0, 0),
    Element("Fluorine", "F", 9, "very high", "low", 18.998, 1.696, 0, 0),
    Element("Neon", "Ne", 10, "low", "high", 20.180, 0.9002, 0, 0),
    # Add the rest of the elements up to Oganesson (element 118)
    Element("Rhenium", "Re", 75, "moderate", "moderate", 186.207, 21.02, 0, 0),
    Element("Osmium", "Os", 76, "moderate", "moderate", 190.23, 22.59, 0, 0),
    Element("Iridium", "Ir", 77, "moderate", "stable", 192.217, 22.56, 0, 0),
    Element("Platinum", "Pt", 78, "moderate", "high", 195.084, 21.45, 0, 0),
    Element("Gold", "Au", 79, "moderate", "stable", 196.967, 19.3, 0, 0),
    Element("Mercury", "Hg", 80, "low", "low", 200.592, 13.53, 0, 0),
    Element("Thallium", "Tl", 81, "moderate", "low", 204.38, 11.85, 0, 0),
    Element("Lead", "Pb", 82, "moderate", "moderate", 207.2, 11.34, 0, 0),
    Element("Bismuth", "Bi", 83, "moderate", "moderate", 208.980, 9.78, 0, 0),
    Element("Polonium", "Po", 84, "high", "low", 209, 9.196, 0, 0),
    Element("Astatine", "At", 85, "high", "low", 210, 7, 0, 0),
    Element("Radon", "Rn", 86, "low", "low", 222, 9.73, 0, 0),
    Element("Francium", "Fr", 87, "very high", "low", 223, 1.87, 0, 0),
    Element("Radium", "Ra", 88, "high", "low", 226, 5.5, 0, 0),
    Element("Actinium", "Ac", 89, "moderate", "moderate", 227, 10.07, 0, 0),
    Element("Thorium", "Th", 90, "moderate", "moderate", 232.038, 11.72, 0, 0),
    Element("Protactinium", "Pa", 91, "moderate", "low", 231.035, 15.37, 0, 0),
    Element("Uranium", "U", 92, "moderate", "low", 238.028, 18.95, 0, 0),
    Element("Neptunium", "Np", 93, "moderate", "low", 237, 20.45, 0, 0),
    Element("Plutonium", "Pu", 94, "moderate", "low", 244, 19.84, 0, 0),
    Element("Americium", "Am", 95, "moderate", "low", 243, 13.67, 0, 0),
    Element("Curium", "Cm", 96, "moderate", "low", 247, 13.51, 0, 0),
    Element("Berkelium", "Bk", 97, "moderate", "low", 247, 14.78, 0, 0),
    Element("Californium", "Cf", 98, "moderate", "low", 251, 15.1, 0, 0),
    Element("Einsteinium", "Es", 99, "moderate", "low", 252, 8.84, 0, 0),
    Element("Fermium", "Fm", 100, "moderate", "low", 257, 8.7, 0, 0),
    Element("Mendelevium", "Md", 101, "moderate", "low", 258, 10.3, 0, 0),
    Element("Nobelium", "No", 102, "moderate", "low", 259, 9.9, 0, 0),
    Element("Lawrencium", "Lr", 103, "moderate", "low", 262, 15.6, 0, 0),
    Element("Rutherfordium", "Rf", 104, "moderate", "low", 267, 23.2, 0, 0),
    Element("Dubnium", "Db", 105, "moderate", "low", 270, 29.3, 0, 0),
    Element("Seaborgium", "Sg", 106, "moderate", "low", 271, 35.3, 0, 0),
    Element("Bohrium", "Bh", 107, "high", "low", 274, 37.1, 0, 0),
    Element("Hassium", "Hs", 108, "high", "low", 277, 40.7, 0, 0),
    Element("Meitnerium", "Mt", 109, "moderate", "low", 278, 48.6, 0, 0),
    Element("Darmstadtium", "Ds", 110, "moderate", "low", 281, 54.1, 0, 0),
    Element("Roentgenium", "Rg", 111, "moderate", "low", 282, 57.6, 0, 0),
    Element("Copernicium", "Cn", 112, "moderate", "low", 285, 64.5, 0, 0),
    Element("Nihonium", "Nh", 113, "moderate", "low", 286, 67.7, 0, 0),
    Element("Flerovium", "Fl", 114, "moderate", "low", 289, 71.8, 0, 0),
    Element("Moscovium", "Mc", 115, "moderate", "low", 290, 77.4, 0, 0),
    Element("Livermorium", "Lv", 116, "moderate", "low", 293, 81.4, 0, 0),
    Element("Tennessine", "Ts", 117, "moderate", "low", 294, 21.6, 0, 0),
    Element("Oganesson", "Og", 118, "moderate", "low", 294, 12.7, 0, 0)
]

# Export the periodic table
def get_periodic_table():
    return periodic_table
