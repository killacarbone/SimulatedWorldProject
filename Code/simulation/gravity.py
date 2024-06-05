import logging

class Gravity:
    GRAVITY_CONSTANT = 9.81  # Simplified gravity constant

    @staticmethod
    def apply(elements):
        for element in elements:
            if element.mass > 0:
                acceleration = Gravity.GRAVITY_CONSTANT / element.mass  # Mass-dependent gravity effect
                element.position_y -= acceleration
                logging.info(f"Gravity applied to element {element.symbol}: new position ({element.position_x}, {element.position_y})")
            else:
                logging.warning(f"Element {element.symbol} has zero mass, skipping gravity application.")
