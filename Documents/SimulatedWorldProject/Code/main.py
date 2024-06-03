from simulation.element import Element
from simulation.world import World

def main():
    # Create a new world instance
    world = World()

    # Define elements
    elements = [
        Element("Hydrogen", "H", 1, "high", "low"),
        Element("Oxygen", "O", 8, "very high", "high"),
        Element("Carbon", "C", 6, "high", "high"),
        Element("Nitrogen", "N", 7, "moderate", "high"),
        Element("Sulfur", "S", 16, "moderate", "high")
    ]

    # Add elements to the world
    for element in elements:
        world.add_element(element)

    # Simulate the passage of time
    for time_step in range(10):  # Simulate 10 time steps
        print(f"\nTime step: {time_step}")
        world.trigger_random_event()
        world.print_summary()

if __name__ == "__main__":
    main()
