import time
import random
from simulation.world import World
from simulation.element import Element

def main():
    # Initialize your world here
    world = World()

    # Adding some example elements
    hydrogen = Element("Hydrogen", "H", 1, "high", "low", random.randint(0, 100), random.randint(0, 100))
    oxygen = Element("Oxygen", "O", 8, "high", "low", random.randint(0, 100), random.randint(0, 100))
    world.add_element(hydrogen)
    world.add_element(oxygen)

    try:
        while True:
            world.time_step()
            time.sleep(1)  # Adjust this interval as needed
    except KeyboardInterrupt:
        print("Simulation stopped by user.")

if __name__ == "__main__":
    main()
