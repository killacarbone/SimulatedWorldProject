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

    # Define core emotions
    core_emotions = {
        "happiness": 0,
        "sadness": 0,
        "anger": 0,
        "fear": 0,
        "disgust": 0,
        "surprise": 0,
    }

    # Add an entity to the world with emotions
    entity = Entity("Entity1", core_emotions)
    world.add_entity(entity)
    print(world)

    # Update the world
    world.update()

    # Perform action with the entity
    entity.perform_action()

    # Print the entity's emotions
    print(entity)

if __name__ == "__main__":
    main()
