import math
import logging

class Physics:
    def apply_gravity(self, elements):
        for element in elements:
            element.position_y -= 1  # Simplified gravity effect
            logging.info(f"Gravity applied to element {element.symbol}: new position ({element.position_x}, {element.position_y})")

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
            if element.temperature > element.melting_point:
                element.state = 'liquid'
            elif element.temperature > element.boiling_point:
                element.state = 'gas'
            logging.info(f"Thermal dynamics applied to element {element.symbol}: state {element.state}, temperature {element.temperature}")
