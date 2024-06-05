import logging

def apply_thermal_dynamics(elements):
    for element in elements:
        if element.temperature > element.melting_point:
            element.state = 'liquid'
        elif element.temperature > element.boiling_point:
            element.state = 'gas'
        else:
            element.state = 'solid'
        logging.info(f"Thermal dynamics applied to element {element.symbol}: state {element.state}, temperature {element.temperature}")
