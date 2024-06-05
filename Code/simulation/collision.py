import logging

class Collision:
    @staticmethod
    def detect_and_resolve(elements, chemistry):
        for i, element1 in enumerate(elements):
            for element2 in elements[i+1:]:
                if Collision.are_colliding(element1, element2):
                    chemistry.form_compound(element1, element2)
                    logging.info(f"Collision detected between {element1.symbol} and {element2.symbol}")

    @staticmethod
    def are_colliding(element1, element2):
        return abs(element1.position_x - element2.position_x) <= 1 and abs(element1.position_y - element2.position_y) <= 1
