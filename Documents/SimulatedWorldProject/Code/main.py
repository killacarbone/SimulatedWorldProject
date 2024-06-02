import numpy as np
from simulation.world import World

class Entity:
    def __init__(self, name):
        self.name = name

    def update(self):
        print(f"{self.name} is being updated")

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

    # Add an entity to the world
    entity = Entity("Entity1")
    world.add_entity(entity)
    print(world)

    # Update the world
    world.update()

if __name__ == "__main__":
    main()

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

    # Add an entity to the world
    entity = Entity("Entity1")
    world.add_entity(entity)
    print(world)

    # Update the world
    world.update()

    # Perform action with the entity
    entity.perform_action()

if __name__ == "__main__":
    main()
