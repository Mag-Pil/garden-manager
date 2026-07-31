class Tree:
    def __init__(self, species, variety, approximate_age):
        self.species = species
        self.variety = variety
        self.approximate_age = int(approximate_age)


def print_tree(tree):
    print(f"Species: {tree.species}, variety: {tree.variety}, approximate age: {tree.approximate_age} years")
