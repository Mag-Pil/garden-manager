import random
from garden_manager.garden.plant import Plant
from garden_manager.garden.planting import Planting
from garden_manager.garden.garden_bed import GardenBed

def random_garden_bed():
    number_of_plants = random.randint(1, 20)

    plantings = []

    for i in range(number_of_plants):
        plant = Plant(
            plant_name=f"Plant-{i + 1}",
            variety="Unknown",
            category="Random",
            plant_spacing=0.25
        )
        planting = Planting(
            plant=plant,
            quantity=random.randint(1, 5)
        )

        plantings.append(planting)

        garden_bed = GardenBed(
            bed_name="Random garden bed",
            list_of_plantings=plantings
        )

    return garden_bed