class Plant:
    def __init__(self, plant_name, variety, category):
        self.plant_name = plant_name
        self.variety = variety
        self.category = category

def print_plant(plant):
    print(f"Nazwa rośliny: {plant.plant_name}, odmiana: {plant.variety}, kategoria: {plant.category}")

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
    print(f"Grządka: {garden_bed.bed_name}")
    print(f"Lista roślin na grządce:")
    for plant in garden_bed.list_of_plants:
        print(f"- {plant.plant_name} {plant.variety}")
    print(f"Liczba roślin na grządce: {garden_bed.number_of_plants}")

class Tree:
    def __init__(self, species, variety, approximate_age):
        self.species = species
        self.variety = variety
        self.approximate_age = int(approximate_age)

def print_tree(tree):
    print(f"Gatunek drzewa: {tree.species}, odmiana: {tree.variety}, przybliżony wiek: {tree.approximate_age} lat")

class GardenTask:
    def __init__(self, task_name, garden_part, execution_status):
        self.task_name = task_name
        self.garden_part = garden_part
        self.execution_status = execution_status

def print_garden_task(garden_task):
    print(f"Nazwa zadania: {garden_task.task_name}")
    print(f"Część ogrodu: {garden_task.garden_part}")
    print(f"Status wykonania: {garden_task.execution_status}")


def run_example():
    calendula = Plant(plant_name="Nagietek", variety="lekarski", category="Kwiaty")
    raspberry_tomato = Plant(plant_name="Pomidor", variety="malinowy", category="Warzywa")
    san_marzano_tomato = Plant(plant_name="Pomidor", variety="San Marzano", category="Warzywa")
    black_hungarian = Plant(plant_name="Papryka", variety="czarna węgierska", category="Warzywa")
    ethiopian_brown = Plant(plant_name="Papryka", variety="etiopska", category="Warzywa")
    beet = Plant(plant_name="Burak", variety="ćwikłowy", category="Warzywa")
    carrot = Plant(plant_name="Marchewka", variety="Berlikumer", category="Warzywa")
    cosmos = Plant(plant_name="Kosmos", variety="pierzasty", category="Kwiaty")
    print_plant(calendula)
    print_plant(raspberry_tomato)
    print_plant(san_marzano_tomato)
    print_plant(black_hungarian)
    print_plant(ethiopian_brown)
    print_plant(beet)
    print_plant(carrot)
    print_plant(cosmos)
    print(10 * "-")

    vegetable_bed_1 = GardenBed(bed_name="Grządka warzywna przy winogronach", list_of_plants=[calendula,raspberry_tomato,san_marzano_tomato,black_hungarian, ethiopian_brown, beet, carrot, cosmos])
    print_garden_bed(vegetable_bed_1)
    print(10 * "-")

    quince_tree_1 = Tree(species="Pigwa", variety="gruszkowa", approximate_age=10)
    print_tree(quince_tree_1)
    quince_tree_2 = Tree(species="Pigwa", variety="gruszkowa", approximate_age=10)
    print_tree(quince_tree_2)
    grafted_chokeberry = Tree(species="Aronia", variety="czarna, szczepiona na jarzębinie", approximate_age=10)
    print_tree(grafted_chokeberry)
    plum_tree = Tree(species="Śliwa", variety="nieznana", approximate_age=10)
    print_tree(plum_tree)
    print(10 * "-")

    tree_pruning_1 = GardenTask(task_name="Przycinanie drzew", garden_part="mniejszy sad", execution_status="odłożone do zimy")
    print_garden_task(tree_pruning_1)

if __name__ == '__main__':
    run_example()

