class Plant:
    def __init__(self, plant_name, variety, category, plant_spacing):
        self.plant_name = plant_name
        self.variety = variety
        self.category = category
        self.plant_spacing = float(plant_spacing)


    def print_plant(self):
        print(f"Plant name: {self.plant_name}, variety: {self.variety}")
        print(f"category: {self.category}, spacing: {self.plant_spacing} m")

    def calculate_area(self, number_of_plants):
        return (self.plant_spacing ** 2) * number_of_plants
