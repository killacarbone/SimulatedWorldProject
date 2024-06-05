import math
import logging

class ElectromagneticForces:
    @staticmethod
    def apply(elements):
        k = 8.99e9  # Coulomb's constant in N m²/C²
        for i, element1 in enumerate(elements):
            for element2 in elements[i+1:]:
                r = math.sqrt((element2.position_x - element1.position_x)**2 + (element2.position_y - element1.position_y)**2)
                if r > 0:
                    force = k * (element1.charge * element2.charge) / r**2
                    logging.info(f"Electromagnetic force between {element1.symbol} and {element2.symbol}: {force} N")
