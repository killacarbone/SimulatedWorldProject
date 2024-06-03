import json
import random
import logging
from collections import defaultdict
from .element import Element
from .element_ratios import get_element_ratios
from .key_compounds import get_key_compounds

# Set up logging
logging.basicConfig(filename="simulation.log", level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class World:
    def __init__(self):
        self.elements = []
        self.compounds = defaultdict(int)  # Use defaultdict to count occurrences of compounds
        self.load_key_compounds()
        self.initialize_elements()

    def add_element(self, element):
        self.elements.append(element)

    def time_step(self, step):
        # Add logic for compound formation with respect to ratios
        for element1 in self.elements:
            for element2 in self.elements:
                if element1 != element2:
                    # Simplified interaction logic for demonstration
                    if element1.reactivity == "high" and element2.reactivity == "high" and random.random() > 0.5:
                        compound_name = f"{element1.symbol}{element2.symbol}"
                        self.compounds[compound_name] += 1
                        logging.info(f"Step {step}: {compound_name} compound formed")
                    elif element1.reactivity == "moderate" and element2.reactivity == "moderate" and random.random() > 0.8:
                        compound_name = f"{element1.symbol}{element2.symbol}"
                        self.compounds[compound_name] += 1
                        logging.info(f"Step {step}: {compound_name} compound formed")
                    elif element1.reactivity == "low" and element2.reactivity == "low" and random.random() > 0.95:
                        compound_name = f"{element1.symbol}{element2.symbol}"
                        self.compounds[compound_name] += 1
                        logging.info(f"Step {step}: {compound_name} compound formed")

    def save_state(self):
        state = {
            "elements": [(e.name, e.symbol, e.atomic_number, e.reactivity, e.stability, e.position_x, e.position_y) for e in self.elements],
            "compounds": dict(self.compounds)
        }
        with open("simulation_state.json", "w") as file:
            json.dump(state, file)
        with open("world_state.json", "w") as file:
            json.dump(state, file)
        print("State saved successfully.")

    def load_state(self):
        try:
            with open("simulation_state.json", "r") as file:
                state = json.load(file)
            self.elements = [Element(*e) for e in state["elements"]]
            self.compounds = defaultdict(int, state["compounds"])
            print("Previous state loaded successfully.")
        except FileNotFoundError:
            print("No previous state found. Initializing with new elements.")

    def load_key_compounds(self):
        key_compounds = get_key_compounds()
        for name, elements in key_compounds:
            self.compounds[name] = 0

    def initialize_elements(self):
        element_ratios = get_element_ratios()
        for symbol, count in element_ratios.items():
            for _ in range(count):
                self.add_element(Element(name=symbol, symbol=symbol, atomic_number=1, reactivity="high", stability="low"))

# Run the simulation
if __name__ == "__main__":
    import time
    world = World()
    try:
        world.load_state()
    except FileNotFoundError:
        hydrogen = Element("Hydrogen", "H", 1, "high", "low", random.randint(0, 100), random.randint(0, 100))
        oxygen = Element("Oxygen", "O", 8, "high", "low", random.randint(0, 100), random.randint(0, 100))
        world.add_element(hydrogen)
        world.add_element(oxygen)

    try:
        step = 0
        while True:
            step += 1
            world.time_step(step)
            if step % 10 == 0:
                print(f"Step {step} completed.")
            time.sleep(0.1)  # Adjust the sleep time to control the simulation speed
    except KeyboardInterrupt:
        print("Simulation stopped by user.")
        world.save_state()
