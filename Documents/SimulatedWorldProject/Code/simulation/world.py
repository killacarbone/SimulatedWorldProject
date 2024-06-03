import json
import random
from collections import defaultdict
from .periodic_table import get_periodic_table
from .element_ratios import get_element_ratios
from .key_compounds import get_key_compounds
from .physics import Physics
from .chemistry import Chemistry
from .element import Element, get_periodic_table


class World:
    def __init__(self):
        self.elements = []
        self.compounds = defaultdict(int)
        self.physics = Physics()
        self.chemistry = Chemistry(self.compounds)
        self.load_key_compounds()
        self.initialize_elements()

    def add_element(self, element):
        self.elements.append(element)

    def time_step(self, step):
        self.physics.apply_gravity(self.elements)
        self.physics.detect_collisions(self.elements, self.chemistry)
        if step % 10 == 0:
            print(f"Step {step} completed.")
        if step % 100 == 0:
            self.save_state()

    def save_state(self):
        state = {
            "elements": [(e.name, e.symbol, e.atomic_number, e.reactivity, e.stability, e.mass, e.position_x, e.position_y, e.velocity_y) for e in self.elements],
            "compounds": list(self.compounds.items())
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
            self.compounds[name] += 1

    def initialize_elements(self):
        element_ratios = get_element_ratios()
        periodic_table = get_periodic_table()
        for symbol, count in element_ratios.items():
            for _ in range(count):
                element = next(e for e in periodic_table if e.symbol == symbol)
                self.add_element(Element(name=element.name, symbol=element.symbol, atomic_number=element.atomic_number, reactivity=element.reactivity, stability=element.stability, mass=element.mass, position_x=random.randint(0, 100), position_y=random.randint(0, 100)))

if __name__ == "__main__":
    import time
    world = World()
    try:
        world.load_state()
    except FileNotFoundError:
        pass

    try:
        step = 0
        while True:
            world.time_step(step)
            step += 1
            time.sleep(1)
    except KeyboardInterrupt:
        print("Simulation stopped by user.")
        world.save_state()
