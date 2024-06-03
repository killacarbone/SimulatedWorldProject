import random
import time
from simulation.world import World
from simulation.element import get_periodic_table

def main():
    world = World()

    try:
        world.load_state()
        print("Previous state loaded successfully.")
    except FileNotFoundError:
        print("No previous state found. Initializing with new elements.")
        for element in get_periodic_table():
            element.position_x = random.randint(0, 100)
            element.position_y = random.randint(0, 100)
            world.add_element(element)

    try:
        for step in range(0, 150, 10):  # Run for 150 steps, logging every 10 steps
            world.time_step(step)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Simulation stopped by user.")
        world.save_state()
        print("State saved successfully.")

if __name__ == "__main__":
    main()
