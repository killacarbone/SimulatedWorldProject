def apply_gravity(elements):
    gravity_constant = 9.81  # Simplified gravity constant
    for element in elements:
        if element.mass > 0:
            acceleration = gravity_constant / element.mass  # Mass-dependent gravity effect
            element.position_y -= acceleration
        else:
            pass
