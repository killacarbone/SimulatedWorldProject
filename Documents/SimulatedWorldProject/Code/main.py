from simulation.world import World
from simulation.element import Element

def main():
    world = World()

    # Adding elements to the world
    hydrogen = Element("Hydrogen", "H", 1, "high", "low")
    oxygen = Element("Oxygen", "O", 8, "very high", "high")
    carbon = Element("Carbon", "C", 6, "high", "high")
    nitrogen = Element("Nitrogen", "N", 7, "moderate", "high")
    sulfur = Element("Sulfur", "S", 16, "moderate", "high")

    world.add_element(hydrogen)
    world.add_element(oxygen)
    world.add_element(carbon)
    world.add_element(nitrogen)
    world.add_element(sulfur)

    # Simulate random events
    random_event = "Oxygen is affected by increased reactivity"
    world.add_event(random_event)
    oxygen.reactivity = "very high"

    # Simulate reactions
    world.simulate_reactions()

    # Print the summary of the world
    world.print_summary()

if __name__ == "__main__":
    main()
