from garden_manager.garden.plant import Plant

class GardenBed:
    def __init__(self, bed_name, list_of_plants=None):
        self.bed_name = bed_name

        if list_of_plants is None:
            list_of_plants = []

        self.list_of_plants = list_of_plants

        number_of_plants = 0
        for plant in list_of_plants:
            number_of_plants += 1

        self.number_of_plants = number_of_plants


def print_garden_bed(garden_bed):
    print(f"Garden bed: {garden_bed.bed_name}")
    print(f"List of plants:")
    for plant in garden_bed.list_of_plants:
        print(f"- {plant.plant_name} {plant.variety}")
    print(f"Number of plants: {garden_bed.number_of_plants}")
