import json

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
with open('Data/periodic_table.json', 'r') as file:
    periodic_table_data = json.load(file)
periodic_table = [Element(**element) for element in periodic_table_data['elements']]

# Load element ratios from JSON
with open('Data/element_ratios.json', 'r') as file:
    element_ratios = json.load(file)['ratios']

# Example usage
for element in periodic_table:
    print(f"{element.name} ({element.symbol}): Mass = {element.mass}, Reactivity = {element.reactivity}")
