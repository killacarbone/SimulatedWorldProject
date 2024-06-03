from simulation.world import World
from simulation.element import Element

def main():
    # Create a world instance
    world = World()

    # Define elements
    hydrogen = Element(name="Hydrogen", symbol="H", atomic_number=1, reactivity="high", stability="low")
    oxygen = Element(name="Oxygen", symbol="O", atomic_number=8, reactivity="moderate", stability="high")
    carbon = Element(name="Carbon", symbol="C", atomic_number=6, reactivity="low", stability="high")

    # Add elements to the world
    world.add_element(hydrogen)
    world.add_element(oxygen)
    world.add_element(carbon)

    # Run the simulation to combine elements
    combined_elements = world.combine_elements()
    print("Combined elements:")
    for compound in combined_elements:
        print(compound)

    # Display the state of the world
    print(world)

if __name__ == "__main__":
    main()
