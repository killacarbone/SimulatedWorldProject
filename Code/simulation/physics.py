from .gravity import apply_gravity
from .collision import detect_collisions
from .electromagnetic_forces import apply_electromagnetic_forces
from .thermal_dynamics import apply_thermal_dynamics

class Physics:
    def apply_gravity(self, elements):
        apply_gravity(elements)
        
    def detect_collisions(self, elements, chemistry):
        detect_collisions(elements, chemistry)
        
    def apply_electromagnetic_forces(self, elements):
        apply_electromagnetic_forces(elements)
        
    def apply_thermal_dynamics(self, elements):
        apply_thermal_dynamics(elements)
