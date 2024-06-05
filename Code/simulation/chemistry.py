import random
import logging

class Chemistry:
    def __init__(self, compounds):
        self.compounds = compounds

    def form_compound(self, element1, element2):
        compound_name = f"{element1.symbol}{element2.symbol}"
        self.compounds[compound_name] += 1
        logging.info(f"Compound formed: {compound_name}")

    def advanced_interactions(self, elements):
        for element in elements:
            if element.temperature > element.melting_point:
                element.state = 'liquid'
            elif element.temperature > element.boiling_point:
                element.state = 'gas'
            else:
                element.state = 'solid'

            if element.state == 'gas' and random.random() > 0.7:
                element.temperature += 1
                logging.info(f"Element {element.symbol} temperature increased due to interaction")

    def log_state(self):
        logging.info(f"Compounds at time step: {self.compounds}")
