class Tree:
    def __init__(self, species, variety, approximate_age):
        self.species = species
        self.variety = variety
        self.approximate_age = int(approximate_age)


    def print_tree(self):
        print(f"Species: {self.species}, variety: {self.variety}, approximate age: {self.approximate_age} years")
