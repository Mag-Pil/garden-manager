import random
from garden_manager.garden.plant import Plant
from garden_manager.garden.garden_bed import GardenBed
from garden_manager.garden.random_generator import random_garden_bed
from garden_manager.garden.tree import Tree
from garden_manager.garden.garden_task import GardenTask
from garden_manager.garden.planting import Planting

def run_example():
    calendula = Plant(plant_name="Calendula", variety="officinalis", category="Flowers", plant_spacing=0.25)
    raspberry_tomato = Plant(plant_name="Tomato", variety="Raspberry", category="Vegetables", plant_spacing=0.5)
    san_marzano_tomato = Plant(plant_name="Tomato", variety="San Marzano", category="Vegetables", plant_spacing=0.5)
    black_hungarian = Plant(plant_name="Pepper", variety="Black Hungarian", category="Vegetables", plant_spacing=0.4)
    ethiopian_brown = Plant(plant_name="Pepper", variety="Ethiopian Brown", category="Vegetables", plant_spacing=0.4)
    beet = Plant(plant_name="Beet", variety="red", category="Vegetables", plant_spacing=0.1)
    carrot = Plant(plant_name="Carrot", variety="Berlikumer", category="Vegetables", plant_spacing=0.05)
    cosmos = Plant(plant_name="Cosmos", variety="bipinnatus", category="Flowers", plant_spacing=0.3)
    calendula_str = str(calendula)
    print(calendula_str)
    raspberry_tomato_str = str(raspberry_tomato)
    print(raspberry_tomato_str)
    san_marzano_tomato_str = str(san_marzano_tomato)
    print(san_marzano_tomato_str)
    black_hungarian_str = str(black_hungarian)
    print(black_hungarian_str)
    ethiopian_brown_str = str(ethiopian_brown)
    print(ethiopian_brown_str)
    beet_str = str(beet)
    print(beet_str)
    carrot_str = str(carrot)
    print(carrot_str)
    cosmos_str = str(cosmos)
    print(cosmos_str)
    print(10 * "-")

    calendula = Plant(plant_name="Calendula", variety="officinalis", category="Flowers", plant_spacing=0.25)
    calendula_copy = Plant(plant_name="Calendula", variety="officinalis", category="Flowers", plant_spacing=0.25)
    print(f"{calendula} \n== {calendula_copy}")
    print(calendula == calendula_copy)
    print(10 * "-")

    raspberry_tomato = Plant(plant_name="Tomato", variety="Raspberry", category="Vegetables", plant_spacing=0.5)
    raspberry_tomato_other_spacing = Plant(plant_name="Tomato", variety="Raspberry", category="Vegetables", plant_spacing=0.6)
    print(f"{raspberry_tomato} \n== {raspberry_tomato_other_spacing}")
    print(raspberry_tomato == raspberry_tomato_other_spacing)
    print(10 * "-")

    vegetable_bed_1 = GardenBed(
        bed_name="Vegetable bed next to the grapevine",
        list_of_plantings=[
            Planting(calendula,3),
            Planting(raspberry_tomato,5),
            Planting(san_marzano_tomato,2),
            Planting(black_hungarian, 2),
            Planting(ethiopian_brown, 2),
            Planting(beet, 10),
            Planting(carrot, 20),
            Planting(cosmos, 3)
        ]
    )
    vegetable_bed_1_str = str(vegetable_bed_1)
    print(vegetable_bed_1_str)
    print(len(vegetable_bed_1))
    print(bool(vegetable_bed_1))
    print(10 * "-")

    vegetable_bed_2 = GardenBed(
        bed_name="Empty vegetable bed",
        list_of_plantings=[]
    )

    vegetable_bed_2_copy = GardenBed(
        bed_name="Empty vegetable bed",
        list_of_plantings=[]
    )

    vegetable_bed_2_str = str(vegetable_bed_2)
    print(vegetable_bed_2_str)
    print(len(vegetable_bed_2))
    print(bool(vegetable_bed_2))
    print(10 * "-")

    print(f"{vegetable_bed_1} \n== \n{vegetable_bed_2}")
    print(vegetable_bed_1 == vegetable_bed_2)
    print(10 * "-")

    print(f"{vegetable_bed_2} \n== \n{vegetable_bed_2_copy}")
    print(vegetable_bed_2 == vegetable_bed_2_copy)
    print(10 * "-")

    raspberry_tomatoes_bed_1 = Planting(plant=raspberry_tomato, quantity=5)
    raspberry_tomatoes_bed_1_str = str(raspberry_tomatoes_bed_1)
    print(raspberry_tomatoes_bed_1_str)
    print(10 * "-")

    raspberry_tomatoes_bed_2 = Planting(plant=raspberry_tomato, quantity=2)
    raspberry_tomatoes_bed_2_str = str(raspberry_tomatoes_bed_2)
    print(raspberry_tomatoes_bed_2_str)
    print(10 * "-")

    all_plants = raspberry_tomatoes_bed_1 + raspberry_tomatoes_bed_2
    print(all_plants)
    print(10 * "-")

    print(f"{raspberry_tomatoes_bed_1} == {raspberry_tomatoes_bed_2}")
    print(raspberry_tomatoes_bed_1 == raspberry_tomatoes_bed_2)
    raspberry_tomatoes_bed_3 = Planting(plant=raspberry_tomato, quantity=5)
    print(f"{raspberry_tomatoes_bed_3} == {raspberry_tomatoes_bed_1}")
    print(raspberry_tomatoes_bed_3 == raspberry_tomatoes_bed_1)
    print(10 * "-")

    random_bed = random_garden_bed()
    random_bed_str = str(random_bed)
    print(random_bed_str)
    print(10 * "-")

    quince_tree_1 = Tree(species="Quince", variety="oblonga", approximate_age=10)
    quince_tree_1_repr = repr(quince_tree_1)
    print(quince_tree_1_repr)
    quince_tree_2 = Tree(species="Quince", variety="oblonga", approximate_age=10)
    quince_tree_2_repr = repr(quince_tree_2)
    print(quince_tree_2_repr)
    grafted_chokeberry = Tree(species="Chokeberry", variety="black", approximate_age=10)
    grafted_chokeberry_str = str(grafted_chokeberry)
    print(grafted_chokeberry_str)
    plum_tree = Tree(species="Plum", variety="unknown", approximate_age=10)
    plum_tree_str = str(plum_tree)
    print(plum_tree_str)
    print(10 * "-")

    tree_pruning_1 = GardenTask(task_name="Tree pruning", garden_part="smaller orchard", execution_status="postponed until winter")
    tree_pruning_1_str = str(tree_pruning_1)
    print(tree_pruning_1_str)

if __name__ == '__main__':
    run_example()
