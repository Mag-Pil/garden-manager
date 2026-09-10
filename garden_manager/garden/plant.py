class Plant:
    def __init__(self, plant_name, variety, category, plant_spacing):
        self.plant_name = plant_name
        self.variety = variety
        self.category = category
        self.plant_spacing = float(plant_spacing)

    def __str__(self):
        return (
            f"Plant name: {self.plant_name}, variety: {self.variety}, "
            f"category: {self.category}, spacing: {self.plant_spacing} m"
        )

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (
            self.plant_name == other.plant_name
            and self.variety == other.variety
            and self.category == other.category
            and self.plant_spacing == other.plant_spacing
        )

    def calculate_area(self, number_of_plants):
        return (self.plant_spacing ** 2) * number_of_plants
