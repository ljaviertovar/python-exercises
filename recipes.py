from os import system
from pathlib import Path

base_path = Path.home()
recipies_dir = Path(base_path, "Recetas")
menu_options = ["Read Recipe", "Add Recipe", "Crete Category", "Delete Recipe", "Delete Category",
                "Exit"]


def get_total_recipes():
    return len(list(Path(recipies_dir).glob("**/*.txt")))


def show_main_menu():
    print("* Main menu\n")
    print("Select an option:")
    menu = ""
    for index, op in enumerate(menu_options):
        menu += f"[{index + 1}] {op}\n"

    selected_option = input(menu)
    while not selected_option.isnumeric() or int(selected_option) not in range(1, len(menu_options) + 1):
        system("cls")
        print("Oops! that option does not exist, select another one:\n")
        selected_option = input(menu)

    return int(selected_option)


def exec_op1(menu_title):
    selected_category, categories_options = get_categories()
    system("cls")

    print(f"* {menu_title}")
    print(f"└── {categories_options[selected_category]}\n")

    selected_recipe, recipe_paths = get_recipies(categories_options[selected_category])
    system("cls")

    print(f"* {menu_title}")
    print(f"└── {categories_options[selected_category]}\n")

    show_recipie(selected_recipe, recipe_paths)


def get_categories():
    categories = Path(recipies_dir)
    option = 1
    categories_options = {}
    menu_categories = ""

    for category in Path(categories).iterdir():
        cat = Path(category).stem
        menu_categories += f"[{option}] {cat}\n"
        categories_options[option] = cat
        option += 1

    selected_category = input(f"Select a category:\n{menu_categories}\n")
    while not selected_category.isnumeric() or int(selected_category) not in range(1, option):
        system("cls")
        print("Oops! that option does not exist, select another one:\n")
        selected_category = input(f"Select a category:\n{menu_categories}\n")

    return int(selected_category), categories_options


def get_recipies(folder):
    category_dir = Path(recipies_dir, folder)
    option = 1
    recipe_paths = {}
    menu_recipies = ""

    for recipie in Path(category_dir).glob("*.txt"):
        rec = Path(recipie).stem
        menu_recipies += f"[{option}] {rec}\n"
        recipe_paths[option] = recipie
        option += 1

    selected_recipe = input(f"Select a recipe:\n{menu_recipies}")
    while not selected_recipe.isnumeric() or int(selected_recipe) not in range(1, option):
        system("cls")
        print("Oops! that option does not exist, select another one:\n")
        selected_recipe = input(f"Select a recipe:\n{menu_recipies}")

    return int(selected_recipe), recipe_paths


def show_recipie(selected_recipe, recipe_paths):
    recipe_path = recipe_paths[selected_recipe]
    recipe = open(Path(recipe_path))
    print(f"{Path(recipe_path).stem}:")
    print(recipe.read())
    recipe.close()


def exec_op2(menu_title):
    selected_category, categories_options = get_categories()
    system("cls")

    print(f"* {menu_title}")
    print(f"└── {categories_options[selected_category]}\n")

    add_recipe(categories_options[selected_category])


def add_recipe(category):
    category_path = Path(category)

    recipe_name = input("Write the title: ")
    while recipe_name == "":
        recipe_name = input("Write the title: ")

    content_recipe = input("Write the content: ")
    while content_recipe == "":
        content_recipe = input("Write the content: ")

    new_recipe_path = Path(recipies_dir, category_path, recipe_name + ".txt")
    recipe_file = open(new_recipe_path, "w")
    recipe_file.write(content_recipe)
    recipe_file.close()

    system("cls")
    print("Recipe created!")


def exec_op3():
    add_category()


def add_category():
    category_title = input("Write the title: ")
    while category_title == "":
        category_title = input("Write the title: ")

    Path(recipies_dir, category_title).mkdir(parents=True, exist_ok=True)


def exec_op4(menu_title):
    selected_category, categories_options = get_categories()
    system("cls")

    print(f"* {menu_title}")
    print(f"└── {categories_options[selected_category]}\n")

    selected_recipe, recipe_paths = get_recipies(categories_options[selected_category])
    system("cls")

    print(f"* {menu_title}")
    print(f"└── {categories_options[selected_category]}\n")

    delete_recipie(selected_recipe, recipe_paths)


def delete_recipie(selected_recipe, recipe_paths):
    recipe_to_delete_path = Path(recipe_paths[selected_recipe])
    recipe_to_delete_path.unlink()
    system("cls")
    print("Recipe deleted!")


def exec_op5(menu_title):
    selected_category, categories_options = get_categories()
    system("cls")

    delete_category(selected_category, categories_options)


def delete_category(selected_category, categories_options):
    category_to_delete_path = Path(recipies_dir, categories_options[selected_category])
    rm_tree(category_to_delete_path)

    system("cls")
    print("Category deleted!")


def rm_tree(directory_path: Path):
    for child in directory_path.iterdir():
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)

    directory_path.rmdir()


def exec_recipies(option):
    menu_title = menu_options[option - 1]
    print(f"* {menu_title}\n")

    match option:
        case 1:
            exec_op1(menu_title)
        case 2:
            exec_op2(menu_title)
        case 3:
            exec_op3()
        case 4:
            exec_op4(menu_title)
        case 5:
            exec_op5(menu_title)
    print("\n**********************************************\n")


def init():
    print("\n**********************************************\n")
    print("Hi buddy!")
    print(f"You can find the recipes in : {recipies_dir}")
    print(f"we have {get_total_recipes()} recipe(s).")
    print("\n**********************************************\n")

    option = show_main_menu()
    system('cls')

    while option != 6:
        exec_recipies(option)
        option = show_main_menu()
        system('cls')

    print("Bye!")


init()
