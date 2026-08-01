import random
from garden_manager.garden.plant import Plant
from garden_manager.garden.garden_bed import GardenBed
from garden_manager.garden.random_generator import random_garden_bed
from garden_manager.garden.tree import Tree
from garden_manager.garden.garden_task import GardenTask

def run_example():
    calendula = Plant(plant_name="Calendula", variety="officinalis", category="Flowers", plant_spacing=0.25)
    raspberry_tomato = Plant(plant_name="Tomato", variety="Raspberry", category="Vegetables", plant_spacing=0.5)
    san_marzano_tomato = Plant(plant_name="Tomato", variety="San Marzano", category="Vegetables", plant_spacing=0.5)
    black_hungarian = Plant(plant_name="Pepper", variety="Black Hungarian", category="Vegetables", plant_spacing=0.4)
    ethiopian_brown = Plant(plant_name="Pepper", variety="Ethiopian Brown", category="Vegetables", plant_spacing=0.4)
    beet = Plant(plant_name="Beet", variety="red", category="Vegetables", plant_spacing=0.1)
    carrot = Plant(plant_name="Carrot", variety="Berlikumer", category="Vegetables", plant_spacing=0.05)
    cosmos = Plant(plant_name="Cosmos", variety="bipinnatus", category="Flowers", plant_spacing=0.3)
    calendula.print_plant()
    raspberry_tomato.print_plant()
    san_marzano_tomato.print_plant()
    black_hungarian.print_plant()
    ethiopian_brown.print_plant()
    beet.print_plant()
    carrot.print_plant()
    cosmos.print_plant()
    print(10 * "-")

    vegetable_bed_1 = GardenBed(bed_name="Vegetable bed next to the grapevine", list_of_plants=[calendula,raspberry_tomato,san_marzano_tomato,black_hungarian, ethiopian_brown, beet, carrot, cosmos])
    vegetable_bed_1.print_garden_bed()
    print(10 * "-")

    random_bed = random_garden_bed()
    random_bed.print_garden_bed()
    print(10 * "-")

    quince_tree_1 = Tree(species="Quince", variety="oblonga", approximate_age=10)
    quince_tree_1.print_tree()
    quince_tree_2 = Tree(species="Quince", variety="oblonga", approximate_age=10)
    quince_tree_2.print_tree()
    grafted_chokeberry = Tree(species="Chokeberry", variety="black", approximate_age=10)
    grafted_chokeberry.print_tree()
    plum_tree = Tree(species="Plum", variety="unknown", approximate_age=10)
    plum_tree.print_tree()
    print(10 * "-")

    tree_pruning_1 = GardenTask(task_name="Tree pruning", garden_part="smaller orchard", execution_status="postponed until winter")
    tree_pruning_1.print_garden_task()

if __name__ == '__main__':
    run_example()
