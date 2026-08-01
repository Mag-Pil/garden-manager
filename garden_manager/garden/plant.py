class Plant:
    def __init__(self, plant_name, variety, category):
        self.plant_name = plant_name
        self.variety = variety
        self.category = category


    def print_plant(self):
        print(f"Plant name: {self.plant_name}, variety: {self.variety}, category: {self.category}")
