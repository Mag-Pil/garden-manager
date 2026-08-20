from garden_manager.garden.plant import Plant
from garden_manager.garden.planting import Planting

class GardenBed:
    def __init__(self, bed_name, list_of_plantings=None):
        self.bed_name = bed_name

        if list_of_plantings is None:
            list_of_plantings = []

        self.list_of_plantings = list_of_plantings

        number_of_plants = 0
        for planting in list_of_plantings:
            number_of_plants += planting.quantity

        self.number_of_plants = number_of_plants

    def calculate_required_area(self):
        total_area = 0

        for planting in self.list_of_plantings:
            total_area += planting.calculate_required_area()

        return total_area



    def print_garden_bed(self):
        print(f"Garden bed: {self.bed_name}")
        print(f"Plantings:")
        for planting in self.list_of_plantings:
            planting.print_planting()

        print(f"Number of plants: {self.number_of_plants}")
        print(f"Required ares: {self.calculate_required_area():.2f} m2")

