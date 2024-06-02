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

    # Define emotions
    emotions = ["Love", "Hate", "Neutrality"]

    # Add gods (entities) to the world with emotions
    god_love = Entity("God of Love", emotions[0])
    god_hate = Entity("God of Hate", emotions[1])
    god_neutrality = Entity("God of Neutrality", emotions[2])

    world.add_entity(god_love)
    world.add_entity(god_hate)
    world.add_entity(god_neutrality)

    print(world)

    # Update the world
    world.update()

    # Perform actions with the gods
    god_love.perform_action()
    god_hate.perform_action()
    god_neutrality.perform_action()

    # Propose a change to the world
    proposal = "Introduce an act of love"
    world.propose_change(proposal)

    proposal = "Introduce an act of hate"
    world.propose_change(proposal)

    proposal = "Introduce a neutral act"
    world.propose_change(proposal)

    # Print the gods' emotions
    print(god_love)
    print(god_hate)
    print(god_neutrality)

if __name__ == "__main__":
    main()
