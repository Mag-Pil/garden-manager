class Planting:
    def __init__(self, plant, quantity):
        self.plant = plant
        self.quantity = quantity

    def __int__(self):
        return self.quantity

    def __float__(self):
        return self.quantity * (self.plant.plant_spacing ** 2)

    def __add__(self, other):
        all_plants = int(self) + int(other)
        return all_plants

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.plant == other.plant and self.quantity == other.quantity

    def __str__(self):
        return (
            f"{self.quantity} x "
            f"{self.plant.plant_name} {self.plant.variety}, "
            f"required area: {float(self):.2f} m2"
        )
