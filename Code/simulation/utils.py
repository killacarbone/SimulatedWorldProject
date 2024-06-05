import json
from simulation.element import Element

def load_periodic_table():
    with open('Data/periodic_table.json', 'r') as file:
        periodic_table_data = json.load(file)
    return [Element(**element) for element in periodic_table_data['elements']]

def load_element_ratios():
    with open('Data/element_ratios.json', 'r') as file:
        return json.load(file)['ratios']

def load_key_compounds():
    with open('Data/key_compounds.json', 'r') as file:
        return json.load(file)['compounds']
