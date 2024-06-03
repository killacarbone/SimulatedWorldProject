from simulation.world import World
from simulation.element import Element

def main():
    world = World()

    # Adding elements to the world
    hydrogen = Element("Hydrogen", "H", 1, "high", "low")
    oxygen = Element("Oxygen", "O", 8, "moderate", "high")
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

    # Adding compounds to the world
    water = f"Water (H2O) composed of {hydrogen.symbol} + {oxygen.symbol}"
    carbon_dioxide = f"Carbon Dioxide (CO2) composed of {oxygen.symbol} + {carbon.symbol}"
    ammonia = f"Ammonia (NH3) composed of {nitrogen.symbol} + {hydrogen.symbol}"
    methane = f"Methane (CH4) composed of {carbon.symbol} + {hydrogen.symbol}"
    sulfur_dioxide = f"Sulfur Dioxide (SO2) composed of {sulfur.symbol} + {oxygen.symbol}"

    world.add_compound(water)
    world.add_compound(carbon_dioxide)
    world.add_compound(ammonia)
    world.add_compound(methane)
    world.add_compound(sulfur_dioxide)

    # Print the summary of the world
    world.print_summary()

if __name__ == "__main__":
    main()
