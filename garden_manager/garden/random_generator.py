import random
from garden_manager.garden.plant import Plant
from garden_manager.garden.garden_bed import GardenBed

def random_garden_bed():
    number_of_plants = random.randint(1, 20)

    plants = []

    for i in range(number_of_plants):
        plant = Plant(
            plant_name=f"Plant-{i + 1}",
            variety="Unknown",
            category="Random",
            plant_spacing=0.25
        )
        plants.append(plant)

    garden_bed = GardenBed(
        bed_name="Random garden bed",
        list_of_plants=plants
    )

    return garden_bed