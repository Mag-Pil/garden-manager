class Plant:
    def __init__(self, plant_name, variety, category):
        self.plant_name = plant_name
        self.variety = variety
        self.category = category


def print_plant(plant):
    print(f"Plant name: {plant.plant_name}, variety: {plant.variety}, category: {plant.category}")
