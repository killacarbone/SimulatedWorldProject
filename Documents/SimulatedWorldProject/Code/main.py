import numpy as np
from simulation.world import World, Entity

def main():
    # Create a simple NumPy array
    array = np.array([1, 2, 3, 4, 5])
    print("NumPy Array:", array)

    # Perform a simple operation
    sum_of_elements = np.sum(array)
    print("Sum of elements:", sum_of_elements)

    # Create a World instance
    world = World()
    print(world)

    # Define gods with their emotions and values
    god_love = Entity("God of Love", "Love", ["kindness", "compassion", "unity"])
    god_hate = Entity("God of Hate", "Hate", ["conflict", "division", "anger"])
    god_wisdom = Entity("God of Wisdom", "Wisdom", ["balance", "knowledge", "reason"])

    # Add gods (entities) to the world
    world.add_entity(god_love)
    world.add_entity(god_hate)
    world.add_entity(god_wisdom)

    print(world)

    # Update the world
    world.update()

    # Perform actions with the gods
    god_love.perform_action()
    god_hate.perform_action()
    god_wisdom.perform_action()

    # Propose changes to the world
    proposals = [
        "Introduce an act of kindness",
        "Introduce an act of conflict",
        "Introduce a balanced approach"
    ]

    for proposal in proposals:
        world.propose_change(proposal)

    # Print the gods' emotions and values
    print(god_love)
    print(god_hate)
    print(god_wisdom)

if __name__ == "__main__":
    main()
