import json
import random
import logging
from collections import defaultdict
from .element import Element
from .element_ratios import get_element_ratios
from .key_compounds import get_key_compounds
from .periodic_table import get_periodic_table
from .physics import Physics
from .chemistry import Chemistry

class World:
    def __init__(self):
        self.elements = []
        self.compounds = defaultdict(int)
        self.load_key_compounds()
        self.initialize_elements()
        self.physics = Physics()
        self.chemistry = Chemistry(self.compounds)

    def add_element(self, element):
        self.elements.append(element)

    def time_step(self, step):
        self.chemistry.time_step_counter = step
        self.physics.apply_gravity(self.elements)
        self.physics.apply_electromagnetic_forces(self.elements)
        self.physics.apply_thermal_dynamics(self.elements)
        self.physics.detect_collisions(self.elements, self.chemistry)
        self.chemistry.log_state()

    def save_state(self):
        state = {
            "elements": [(e.name, e.symbol, e.atomic_number, e.reactivity, e.stability, e.mass, e.volume, e.charge, e.temperature, e.melting_point, e.boiling_point, e.state, e.position_x, e.position_y) for e in self.elements],
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
            self.compounds[name] += 1

    def initialize_elements(self):
        element_ratios = get_element_ratios()
        periodic_table = get_periodic_table()
        for symbol, count in element_ratios.items():
            for _ in range(count):
                element = next((e for e in periodic_table if e.symbol == symbol), None)
                if element:
                    self.add_element(element)
                else:
                    print(f"Element {symbol} not found in periodic table.")
