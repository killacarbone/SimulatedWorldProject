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
                    logging.info(f"Collision detected between {element1.symbol} and {element2.symbol}")
                    chemistry.form_compound(element1, element2)

    def are_colliding(self, element1, element2):
        return abs(element1.position_x - element2.position_x) <= 1 and abs(element1.position_y - element2.position_y) <= 1
