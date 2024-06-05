# key_compounds.py
# This module provides functions to get key compounds for the simulated world project

# Note: The key compounds are essential compounds that should be tracked and updated in the world simulation.
# They are used to ensure the consistency and accuracy of the simulation's chemical processes.

def get_key_compounds():
    """
    Returns a dictionary of key compounds with their initial counts.
    This function is used to initialize the compounds in the world simulation.
    """
    key_compounds = {
        'H2O': 0,  # Water
        'CO2': 0,  # Carbon Dioxide
        'O2': 0,  # Oxygen
        'N2': 0,  # Nitrogen
        'CH4': 0,  # Methane
        'NH3': 0,  # Ammonia
        'H2SO4': 0,  # Sulfuric Acid
        'C6H12O6': 0,  # Glucose
        'NaCl': 0,  # Sodium Chloride
        'HCl': 0,  # Hydrochloric Acid
        'H2': 0,  # Hydrogen Gas
        'NO2': 0,  # Nitrogen Dioxide
        'SO2': 0,  # Sulfur Dioxide
        'C2H6': 0,  # Ethane
        'C2H4': 0,  # Ethylene
        'C2H2': 0,  # Acetylene
    }
    return key_compounds

# You can also include a more detailed representation of the compounds if needed.
# For example, with their molecular structures or specific properties.
key_compounds_details = {
    'H2O': ['H', 'H', 'O'],  # Water
    'CO2': ['C', 'O', 'O'],  # Carbon Dioxide
    'O2': ['O', 'O'],  # Oxygen
    'N2': ['N', 'N'],  # Nitrogen
    'CH4': ['C', 'H', 'H', 'H', 'H'],  # Methane
    'NH3': ['N', 'H', 'H', 'H'],  # Ammonia
    'H2SO4': ['H', 'H', 'S', 'O', 'O', 'O', 'O'],  # Sulfuric Acid
    'C6H12O6': ['C', 'C', 'C', 'C', 'C', 'C', 'H', 'H', 'H', 'H', 'H', 'H', 'O', 'O', 'O', 'O', 'O', 'O'],  # Glucose
    'NaCl': ['Na', 'Cl'],  # Sodium Chloride
    'HCl': ['H', 'Cl'],  # Hydrochloric Acid
    'H2': ['H', 'H'],  # Hydrogen Gas
    'NO2': ['N', 'O', 'O'],  # Nitrogen Dioxide
    'SO2': ['S', 'O', 'O'],  # Sulfur Dioxide
    'C2H6': ['C', 'C', 'H', 'H', 'H', 'H', 'H', 'H'],  # Ethane
    'C2H4': ['C', 'C', 'H', 'H', 'H', 'H'],  # Ethylene
    'C2H2': ['C', 'C', 'H', 'H'],  # Acetylene
    # Add more key compounds as necessary
}
