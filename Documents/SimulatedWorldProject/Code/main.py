import random
import time
import logging
from simulation.world import World

# Setup logging
logging.basicConfig(filename="simulation.log", level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def main():
    world = World()

    try:
        world.load_state()
        logging.info("Previous state loaded successfully.")
    except FileNotFoundError:
        logging.info("No previous state found. Initializing with new elements.")
        # Add elements from the periodic table dynamically
        for element in get_periodic_table():
            element.position_x = random.randint(0, 100)
            element.position_y = random.randint(0, 100)
            world.add_element(element)

    try:
        step = 0
        while True:
            world.time_step(step)
            step += 1
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Simulation stopped by user.")
        world.save_state()
        logging.info("State saved successfully.")

if __name__ == "__main__":
    main()
