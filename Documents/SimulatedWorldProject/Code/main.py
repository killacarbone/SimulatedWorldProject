import numpy as np
from simulation.world import World

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

if __name__ == "__main__":
    main()
