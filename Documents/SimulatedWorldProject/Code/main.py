import random
import time
from simulation.world import World
from simulation.element import get_periodic_table

def main():
    # Initialize your world here
    world = World()

    try:
        world.load_state()
        print("Previous state loaded successfully.")
    except FileNotFoundError:
        print("No previous state found. Initializing with new elements.")
        # Add elements from the periodic table dynamically
        for element in get_periodic_table():
            # Assign random positions to the elements
            element.position_x = random.randint(0, 100)
            element.position_y = random.randint(0, 100)
            world.add_element(element)

    try:
        step = 0
        while True:
            # Perform a time step in the simulation
            world.time_step()
            step += 1
            if step % 10 == 0:  # Only log every 10 steps to reduce log size
                print(f"Step {step} completed.")
            # Sleep for a bit to slow down the loop (adjust as needed)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Simulation stopped by user.")
        world.save_state()
        print("State saved successfully.")

if __name__ == "__main__":
    main()
