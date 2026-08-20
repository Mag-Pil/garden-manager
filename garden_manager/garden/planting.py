class Planting:
    def __init__(self, plant, quantity):
        self.plant = plant
        self.quantity = quantity

    def calculate_required_area(self):
        return self.quantity * (self.plant.plant_spacing ** 2)

    def print_planting(self):
        print(
            f"{self.quantity} x "
            f"{self.plant.plant_name} {self.plant.variety},"
            f"required area: {self.calculate_required_area():.2f} m2"
        )
