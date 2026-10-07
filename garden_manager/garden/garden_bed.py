from garden_manager.garden.plant import Plant
from garden_manager.garden.planting import Planting

class GardenBed:
    def __init__(self, bed_name, capacity, list_of_plantings=None):
        self.bed_name = bed_name
        self.capacity = float(capacity)

        if list_of_plantings is None:
            list_of_plantings = []

        self.__list_of_plantings = list_of_plantings

    def add_plant_to_gardenbed(self, plant, quantity):
        new_plant = Planting(plant, quantity)

        for planting in self.__list_of_plantings:
            if planting.plant == plant:
                planting.quantity += quantity
                break
        else:
            self.__list_of_plantings.append(new_plant)

        if float(self) >= self.capacity:
            print(f"There's no space for more plants! This garden bed can hold {self.capacity} m2!")


    def __len__(self):
        number_of_plants = 0
        for planting in self.__list_of_plantings:
            number_of_plants += int(planting)

        return number_of_plants

    def __float__(self):
        total_area = 0.0

        for planting in self.__list_of_plantings:
            total_area += float(planting)

        return total_area

    def __str__(self):
        planting_txt = ""
        for planting in self.__list_of_plantings:
            planting_txt += str(planting) + "\n"

        return (
            f"Garden bed: {self.bed_name}\n"
            f"Plantings:\n"
            f"{planting_txt}"
            f"Number of plants: {len(self)}\n"
            f"Required area: {float(self):.2f} m2"
        )