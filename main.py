class Plant:
    def __init__(self, plant_name, variety, category):
        self.plant_name = plant_name
        self.variety = variety
        self.category = category


def print_plant(plant):
    print(f"Plant name: {plant.plant_name}, variety: {plant.variety}, category: {plant.category}")

class GardenBed:
    def __init__(self, bed_name, list_of_plants=None):
        self.bed_name = bed_name

        if list_of_plants is None:
            list_of_plants = []

        self.list_of_plants = list_of_plants

        number_of_plants = 0
        for plant in list_of_plants:
            number_of_plants += 1

        self.number_of_plants = number_of_plants


def print_garden_bed(garden_bed):
    print(f"Garden bed: {garden_bed.bed_name}")
    print(f"List of plants:")
    for plant in garden_bed.list_of_plants:
        print(f"- {plant.plant_name} {plant.variety}")
    print(f"Number of plants: {garden_bed.number_of_plants}")

class Tree:
    def __init__(self, species, variety, approximate_age):
        self.species = species
        self.variety = variety
        self.approximate_age = int(approximate_age)


def print_tree(tree):
    print(f"Species: {tree.species}, variety: {tree.variety}, approximate age: {tree.approximate_age} years")

class GardenTask:
    def __init__(self, task_name, garden_part, execution_status):
        self.task_name = task_name
        self.garden_part = garden_part
        self.execution_status = execution_status


def print_garden_task(garden_task):
    print(f"Task name: {garden_task.task_name}")
    print(f"Garden part: {garden_task.garden_part}")
    print(f"Execution status: {garden_task.execution_status}")


def run_example():
    calendula = Plant(plant_name="Calendula", variety="officinalis", category="Flowers")
    raspberry_tomato = Plant(plant_name="Tomato", variety="Raspberry", category="Vegetables")
    san_marzano_tomato = Plant(plant_name="Tomato", variety="San Marzano", category="Vegetables")
    black_hungarian = Plant(plant_name="Pepper", variety="Black Hungarian", category="Vegetables")
    ethiopian_brown = Plant(plant_name="Pepper", variety="Ethiopian Brown", category="Vegetables")
    beet = Plant(plant_name="Beet", variety="red", category="Vegetables")
    carrot = Plant(plant_name="Carrot", variety="Berlikumer", category="Vegetables")
    cosmos = Plant(plant_name="Cosmos", variety="bipinnatus", category="Flowers")
    print_plant(calendula)
    print_plant(raspberry_tomato)
    print_plant(san_marzano_tomato)
    print_plant(black_hungarian)
    print_plant(ethiopian_brown)
    print_plant(beet)
    print_plant(carrot)
    print_plant(cosmos)
    print(10 * "-")

    vegetable_bed_1 = GardenBed(bed_name="Vegetable bed next to the grapevine", list_of_plants=[calendula,raspberry_tomato,san_marzano_tomato,black_hungarian, ethiopian_brown, beet, carrot, cosmos])
    print_garden_bed(vegetable_bed_1)
    print(10 * "-")

    quince_tree_1 = Tree(species="Quince", variety="oblonga", approximate_age=10)
    print_tree(quince_tree_1)
    quince_tree_2 = Tree(species="Quince", variety="oblonga", approximate_age=10)
    print_tree(quince_tree_2)
    grafted_chokeberry = Tree(species="Chokeberry", variety="black", approximate_age=10)
    print_tree(grafted_chokeberry)
    plum_tree = Tree(species="Plum", variety="unknown", approximate_age=10)
    print_tree(plum_tree)
    print(10 * "-")

    tree_pruning_1 = GardenTask(task_name="Tree pruning", garden_part="smaller orchard", execution_status="postponed until winter")
    print_garden_task(tree_pruning_1)

if __name__ == '__main__':
    run_example()

