import random
from garden_manager.garden.plant import Plant
from garden_manager.garden.plant import print_plant
from garden_manager.garden.garden_bed import GardenBed
from garden_manager.garden.garden_bed import print_garden_bed
from garden_manager.garden.random_generator import random_garden_bed
from garden_manager.garden.tree import Tree
from garden_manager.garden.tree import print_tree
from garden_manager.garden.garden_task import GardenTask
from garden_manager.garden.garden_task import print_garden_task
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

    random_bed = random_garden_bed()
    print_garden_bed(random_bed)
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
