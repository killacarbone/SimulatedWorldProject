import logging

class ThermalDynamics:
    @staticmethod
    def apply(elements):
        for element in elements:
            if element.temperature > element.melting_point:
                element.state = 'liquid'
            elif element.temperature > element.boiling_point:
                element.state = 'gas'
            logging.info(f"Thermal dynamics applied to element {element.symbol}: state {element.state}, temperature {element.temperature}")
