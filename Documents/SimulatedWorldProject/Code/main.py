from simulation.world import World
from simulation.element import periodic_table

def main():
    world = World()
    
    print("Adding elements to the world...")
    for element in periodic_table:
        world.add_element(element)
    print("Elements added.")
    
    print("Triggering random event...")
    world.trigger_random_event()
    
    print("Random event triggered. Printing summary...\n")
    world.print_summary()

if __name__ == "__main__":
    main()
