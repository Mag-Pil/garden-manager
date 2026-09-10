class Tree:
    def __init__(self, species, variety, approximate_age):
        self.species = species
        self.variety = variety
        self.approximate_age = int(approximate_age)


    def __str__(self):
        return (
            f"Species: {self.species}, variety: {self.variety}, approximate age: {self.approximate_age} years"
        )

    def __repr__(self):
        return (
            f"<Species: {self.species}, variety: {self.variety}, approximate age: {self.approximate_age} years>"
        )
