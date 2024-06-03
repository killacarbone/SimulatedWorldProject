from simulation.element import Element
from simulation.world import World

def main():
    world = World()

    hydrogen = Element(name="Hydrogen", symbol="H", atomic_number=1, reactivity="high", stability="low")
    oxygen = Element(name="Oxygen", symbol="O", atomic_number=8, reactivity="very high", stability="high")
    carbon = Element(name="Carbon", symbol="C", atomic_number=6, reactivity="high", stability="high")
    nitrogen = Element(name="Nitrogen", symbol="N", atomic_number=7, reactivity="moderate", stability="high")
    sulfur = Element(name="Sulfur", symbol="S", atomic_number=16, reactivity="moderate", stability="high")

    print("Adding elements to the world...")
    world.add_element(hydrogen)
    world.add_element(oxygen)
    world.add_element(carbon)
    world.add_element(nitrogen)
    world.add_element(sulfur)

    print("Elements added. Triggering random event...")
    # Trigger a random event
    world.trigger_random_event()

    print("Random event triggered. Printing summary...")
    # Print summary
    world.print_summary()

if __name__ == "__main__":
    main()
