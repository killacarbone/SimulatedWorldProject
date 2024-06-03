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
    Element("Lithium", "Li", 3, "high", "moderate"),
    Element("Beryllium", "Be", 4, "moderate", "high"),
    Element("Boron", "B", 5, "moderate", "moderate"),
    Element("Carbon", "C", 6, "high", "high"),
    Element("Nitrogen", "N", 7, "moderate", "high"),
    Element("Oxygen", "O", 8, "very high", "high"),
    Element("Fluorine", "F", 9, "very high", "moderate"),
    Element("Neon", "Ne", 10, "low", "high"),
    # Continue adding all known elements up to atomic number 118
    Element("Sodium", "Na", 11, "high", "low"),
    Element("Magnesium", "Mg", 12, "moderate", "moderate"),
    Element("Aluminum", "Al", 13, "moderate", "moderate"),
    Element("Silicon", "Si", 14, "moderate", "high"),
    Element("Phosphorus", "P", 15, "high", "moderate"),
    Element("Sulfur", "S", 16, "high", "moderate"),
    Element("Chlorine", "Cl", 17, "very high", "moderate"),
    Element("Argon", "Ar", 18, "low", "high"),
    Element("Potassium", "K", 19, "high", "low"),
    Element("Calcium", "Ca", 20, "moderate", "moderate"),
    # Add the rest of the elements up to 118
    Element("Scandium", "Sc", 21, "moderate", "moderate"),
    Element("Titanium", "Ti", 22, "moderate", "high"),
    Element("Vanadium", "V", 23, "moderate", "moderate"),
    Element("Chromium", "Cr", 24, "moderate", "moderate"),
    Element("Manganese", "Mn", 25, "moderate", "moderate"),
    Element("Iron", "Fe", 26, "moderate", "moderate"),
    Element("Cobalt", "Co", 27, "moderate", "moderate"),
    Element("Nickel", "Ni", 28, "moderate", "moderate"),
    Element("Copper", "Cu", 29, "moderate", "moderate"),
    Element("Zinc", "Zn", 30, "low", "high"),
    Element("Gallium", "Ga", 31, "moderate", "moderate"),
    Element("Germanium", "Ge", 32, "moderate", "moderate"),
    Element("Arsenic", "As", 33, "moderate", "moderate"),
    Element("Selenium", "Se", 34, "moderate", "moderate"),
    Element("Bromine", "Br", 35, "high", "moderate"),
    Element("Krypton", "Kr", 36, "low", "high"),
    Element("Rubidium", "Rb", 37, "high", "low"),
    Element("Strontium", "Sr", 38, "moderate", "moderate"),
    Element("Yttrium", "Y", 39, "moderate", "moderate"),
    Element("Zirconium", "Zr", 40, "moderate", "high"),
    Element("Niobium", "Nb", 41, "moderate", "moderate"),
    Element("Molybdenum", "Mo", 42, "moderate", "moderate"),
    Element("Technetium", "Tc", 43, "moderate", "low"),
    Element("Ruthenium", "Ru", 44, "moderate", "moderate"),
    Element("Rhodium", "Rh", 45, "moderate", "moderate"),
    Element("Palladium", "Pd", 46, "moderate", "moderate"),
    Element("Silver", "Ag", 47, "moderate", "moderate"),
    Element("Cadmium", "Cd", 48, "low", "moderate"),
    Element("Indium", "In", 49, "moderate", "moderate"),
    Element("Tin", "Sn", 50, "moderate", "moderate"),
    Element("Antimony", "Sb", 51, "moderate", "moderate"),
    Element("Tellurium", "Te", 52, "moderate", "moderate"),
    Element("Iodine", "I", 53, "high", "moderate"),
    Element("Xenon", "Xe", 54, "low", "high"),
    Element("Cesium", "Cs", 55, "very high", "low"),
    Element("Barium", "Ba", 56, "moderate", "moderate"),
    Element("Lanthanum", "La", 57, "moderate", "moderate"),
    Element("Cerium", "Ce", 58, "moderate", "moderate"),
    Element("Praseodymium", "Pr", 59, "moderate", "moderate"),
    Element("Neodymium", "Nd", 60, "moderate", "moderate"),
    Element("Promethium", "Pm", 61, "moderate", "low"),
    Element("Samarium", "Sm", 62, "moderate", "moderate"),
    Element("Europium", "Eu", 63, "moderate", "moderate"),
    Element("Gadolinium", "Gd", 64, "moderate", "moderate"),
    Element("Terbium", "Tb", 65, "moderate", "moderate"),
    Element("Dysprosium", "Dy", 66, "moderate", "moderate"),
    Element("Holmium", "Ho", 67, "moderate", "moderate"),
    Element("Erbium", "Er", 68, "moderate", "moderate"),
    Element("Thulium", "Tm", 69, "moderate", "moderate"),
    Element("Ytterbium", "Yb", 70, "low", "moderate"),
    Element("Lutetium", "Lu", 71, "moderate", "moderate"),
    Element("Hafnium", "Hf", 72, "moderate", "high"),
    Element("Tantalum", "Ta", 73, "moderate", "moderate"),
    Element("Tungsten", "W", 74, "moderate", "high"),
    Element("Rhenium", "Re", 75, "moderate", "moderate"),
    Element("Osmium", "Os", 76, "moderate", "moderate"),
    Element("Iridium", "Ir", 77, "moderate", "moderate"),
    Element("Platinum", "Pt", 78, "moderate", "high"),
    Element("Gold", "Au", 79, "moderate", "moderate"),
    Element("Mercury", "Hg", 80, "low", "low"),
    Element("Thallium", "Tl", 81, "moderate", "low"),
    Element("Lead", "Pb", 82, "moderate", "moderate"),
    Element("Bismuth", "Bi", 83, "moderate", "moderate"),
    Element("Polonium", "Po", 84, "high", "low"),
    Element("Astatine", "At", 85, "high", "low"),
    Element("Radon", "Rn", 86, "low", "low"),
    Element("Francium", "Fr", 87, "very high", "low"),
    Element("Radium", "Ra", 88, "high", "low"),
    Element("Actinium", "Ac", 89, "moderate", "low"),
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
    Element("Bohrium", "Bh", 107, "moderate", "low"),
    Element("Hassium", "Hs", 108, "moderate", "low"),
    Element("Meitnerium", "Mt", 109, "moderate", "low"),
    Element("Darmstadtium", "Ds", 110, "moderate", "low"),
    Element("Roentgenium", "Rg", 111, "moderate", "low"),
    Element("Copernicium", "Cn", 112, "moderate", "low"),
    Element("Nihonium", "Nh", 113, "moderate", "low"),
    Element("Flerovium", "Fl", 114, "moderate", "low"),
    Element("Moscovium", "Mc", 115, "moderate", "low"),
    Element("Livermorium", "Lv", 116, "moderate", "low"),
    Element("Tennessine", "Ts", 117, "moderate", "low"),
    Element("Oganesson", "Og", 118, "moderate", "low"),
]
