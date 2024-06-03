import random
import time
from simulation.world import World
from simulation.periodic_table import get_periodic_table

def main():
    world = World()

    try:
        world.load_state()
        print("Previous state loaded successfully.")
    except FileNotFoundError:
        print("No previous state found. Initializing with new elements.")
        periodic_table = get_periodic_table()
        for element in periodic_table:
            element.position_x = random.randint(0, 100)
            element.position_y = random.randint(0, 100)
            world.add_element(element)

    step = 0
    try:
        while True:
            world.time_step(step)
            step += 1
            time.sleep(1)
    except KeyboardInterrupt:
        print("Simulation stopped by user.")
        world.save_state()
        print("State saved successfully.")

if __name__ == "__main__":
    main()
