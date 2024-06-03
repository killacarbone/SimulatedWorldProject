import math
import logging

class Physics:
    def apply_gravity(self, elements):
        gravity_constant = 9.81  # m/s^2
        for element in elements:
            if element.mass != 0:
                acceleration = gravity_constant / element.mass
                element.position_y -= acceleration
                logging.info(f"Gravity applied to element {element.symbol}: new position ({element.position_x}, {element.position_y})")
            else:
                logging.warning(f"Element {element.symbol} has zero mass, skipping gravity application.")

    def detect_collisions(self, elements, chemistry):
        for i, element1 in enumerate(elements):
            for element2 in elements[i+1:]:
                if self.are_colliding(element1, element2):
                    chemistry.form_compound(element1, element2)
                    logging.info(f"Collision detected between {element1.symbol} and {element2.symbol}")

    def are_colliding(self, element1, element2):
        return abs(element1.position_x - element2.position_x) <= 1 and abs(element1.position_y - element2.position_y) <= 1

    def apply_electromagnetic_forces(self, elements):
        k = 8.99e9  # Coulomb's constant in N m²/C²
        for i, element1 in enumerate(elements):
            for element2 in elements[i+1:]:
                r = math.sqrt((element2.position_x - element1.position_x)**2 + (element2.position_y - element1.position_y)**2)
                if r > 0:
                    force = k * (element1.charge * element2.charge) / r**2
                    logging.info(f"Electromagnetic force between {element1.symbol} and {element2.symbol}: {force} N")

    def apply_thermal_dynamics(self, elements):
        for element in elements:
            initial_state = element.state
            if element.temperature > element.boiling_point:
                element.state = 'gas'
            elif element.temperature > element.melting_point:
                element.state = 'liquid'
            if initial_state != element.state:
                logging.info(f"Thermal dynamics applied to element {element.symbol}: state changed to {element.state}, temperature {element.temperature}")
