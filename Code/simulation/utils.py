import json

def load_periodic_table(file_path):
    with open(file_path, 'r') as file:
        periodic_table_data = json.load(file)
    return periodic_table_data

def load_element_ratios(file_path):
    with open(file_path, 'r') as file:
        element_ratios = json.load(file)['ratios']
    return element_ratios

def load_key_compounds(file_path):
    with open(file_path, 'r') as file:
        key_compounds = json.load(file)
    return key_compounds
