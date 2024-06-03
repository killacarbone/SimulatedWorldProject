from simulation.world import World
from simulation.element import Element

def main():
    # Create a world instance
    world = World()

    # Add elements to the world
    print("Adding elements to the world...")
    elements = [
        Element("Hydrogen", "H", 1, "high", "low"),
        Element("Oxygen", "O", 8, "high", "low"),
        Element("Carbon", "C", 6, "high", "low"),
        Element("Nitrogen", "N", 7, "high", "low"),
        Element("Sulfur", "S", 16, "very high", "low")
    ]
    for element in elements:
        world.add_element(element)
    print("Elements added.")

    # Run the simulation for a number of time steps
    for step in range(10):
        print(f"\nTime step: {step + 1}")
        world.trigger_random_event()
        world.print_summary()

if __name__ == "__main__":
    main()
