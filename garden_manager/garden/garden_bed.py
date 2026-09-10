from garden_manager.garden.plant import Plant
from garden_manager.garden.planting import Planting

class GardenBed:
    def __init__(self, bed_name, list_of_plantings=None):
        self.bed_name = bed_name

        if list_of_plantings is None:
            list_of_plantings = []

        self.list_of_plantings = list_of_plantings

    def __len__(self):
        number_of_plants = 0
        for planting in self.list_of_plantings:
            number_of_plants += int(planting)

        return number_of_plants

    def __float__(self):
        total_area = 0.0

        for planting in self.list_of_plantings:
            total_area += float(planting)

        return total_area

    def __str__(self):
        planting_txt = ""
        for planting in self.list_of_plantings:
            planting_txt += str(planting) + "\n"

        return (
            f"Garden bed: {self.bed_name}\n"
            f"Plantings:\n"
            f"{planting_txt}"
            f"Number of plants: {len(self)}\n"
            f"Required area: {float(self):.2f} m2"
        )

    def __bool__(self):
        return len(self) > 0

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.bed_name == other.bed_name and self.list_of_plantings == other.list_of_plantings
