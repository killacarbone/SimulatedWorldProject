import time
import random
from simulation.world import World
from simulation.element import Element

def main():
    # Initialize your world here
    world = World()

    try:
        world.load_state()
    except FileNotFoundError:
        print("No previous state found. Initializing with new elements.")
        hydrogen = Element("Hydrogen", "H", 1, "high", "low", random.randint(0, 100), random.randint(0, 100))
        oxygen = Element("Oxygen", "O", 8, "high", "low", random.randint(0, 100), random.randint(0, 100))
        world.add_element(hydrogen)
        world.add_element(oxygen)

    try:
        while True:
            # Perform a time step in the simulation
            world.time_step()
            # Sleep for a bit to slow down the loop (adjust as needed)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Simulation stopped by user.")
        world.save_state()

if __name__ == "__main__":
    main()
