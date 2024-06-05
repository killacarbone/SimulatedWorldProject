from .gravity import apply_gravity
from .collision import apply_collision
from .electromagnetic_forces import apply_electromagnetic_forces
from .thermal_dynamics import apply_thermal_dynamics

class Physics:
    def __init__(self):
        pass

    def apply_forces(self, elements, chemistry):
        apply_gravity(elements)
        apply_collision(elements, chemistry)
        apply_electromagnetic_forces(elements)
        apply_thermal_dynamics(elements)
