# element.py
class Element:
    def __init__(self, name, symbol, atomic_number, reactivity, stability, mass, volume, charge=0, temperature=0, melting_point=0, boiling_point=0, state='solid'):
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.reactivity = reactivity
        self.stability = stability
        self.mass = mass
        self.volume = volume
        self.charge = charge
        self.temperature = temperature
        self.melting_point = melting_point
        self.boiling_point = boiling_point
        self.state = state

# Load periodic table from JSON
def load_periodic_table():
    with open('Data/periodic_table.json', 'r') as file:
        periodic_table_data = json.load(file)
    return [Element(**element) for element in periodic_table_data['elements']]

# Load element ratios from JSON
def load_element_ratios():
    with open('Data/element_ratios.json', 'r') as file:
        return json.load(file)['ratios']
