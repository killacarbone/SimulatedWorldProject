from simulation.gravity import Gravity
from simulation.collision import Collision
from simulation.thermal_dynamics import ThermalDynamics
from simulation.electromagnetic_forces import ElectromagneticForces

class Physics:
    def apply_physics(self, elements, chemistry):
        Gravity.apply(elements)
        Collision.detect_and_resolve(elements, chemistry)
        ThermalDynamics.apply(elements)
        ElectromagneticForces.apply(elements)
