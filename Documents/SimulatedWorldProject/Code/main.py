import time
from simulation.world import World

def main():
    # Initialize your world here
    world = World()

    try:
        while True:
            # Perform a time step in the simulation
            world.time_step()

            # Print the summary for the current time step
            world.print_summary()

            # Sleep for a bit to slow down the loop (adjust as needed)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Simulation stopped by user.")

if __name__ == "__main__":
    main()
