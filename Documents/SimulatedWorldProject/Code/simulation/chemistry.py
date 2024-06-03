import logging
from collections import defaultdict

class Chemistry:
    def __init__(self, compounds):
        self.compounds = compounds
        self.time_step_counter = 0

    def form_compound(self, element1, element2):
        compound_name = f"{element1.symbol}{element2.symbol}"
        self.compounds[compound_name] += 1
        logging.info(f"Step {self.time_step_counter}: Compound formed: {compound_name}")

    def log_state(self):
        logging.info(f"Step {self.time_step_counter} completed.")
        for compound, count in self.compounds.items():
            logging.info(f"Compound {compound} count: {count}")
