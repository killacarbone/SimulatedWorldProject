# main.py
from simulation.element import Element
from simulation.world import World

def main():
    # Create some elements
    hydrogen = Element("Hydrogen", "H", 1, "high", "low")
    oxygen = Element("Oxygen", "O", 8, "moderate", "high")
    carbon = Element("Carbon", "C", 6, "high", "high")
    nitrogen = Element("Nitrogen", "N", 7, "moderate", "high")
    sulfur = Element("Sulfur", "S", 16, "moderate", "high")
    
    # Initialize the world
    world = World()
    
    # Add elements to the world
    world.add_element(hydrogen)
    world.add_element(oxygen)
    world.add_element(carbon)
    world.add_element(nitrogen)
    world.add_element(sulfur)
    
    # Combine elements to form compounds
    world.combine_elements()
    
    # Introduce a random event
    world.random_event()
    
    # Print the world state
    print(world)

if __name__ == "__main__":
    main()
