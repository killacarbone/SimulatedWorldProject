import logging

def apply_gravity(elements):
    gravity_constant = 9.81
    for element in elements:
        if element.mass > 0:
            acceleration = gravity_constant / element.mass
            element.position_y -= acceleration
            logging.info(f"Gravity applied to element {element.symbol}: new position ({element.position_x}, {element.position_y})")
        else:
            logging.warning(f"Element {element.symbol} has zero mass, skipping gravity application.")
