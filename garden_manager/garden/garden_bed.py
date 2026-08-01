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


    def print_garden_bed(self):
        print(f"Garden bed: {self.bed_name}")
        print(f"List of plants:")
        for plant in self.list_of_plants:
            print(f"- {plant.plant_name} {plant.variety}")
        print(f"Number of plants: {self.number_of_plants}")
