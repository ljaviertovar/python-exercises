import turn_fn as turner

def show_menu():
    menu = "Select department:\n"
    for d in turner.departments:
        menu += f"[{d}]: {turner.departments[d]}\n"

    menu += "[e] Exit\n"
    return menu


def init():

    option ='x'
    while option != 'e':
        try:
            print(show_menu())
            option = input()
            ["d","p","c"].index(option)
            turner.decorate_turn(option)

        except ValueError:
            print("Department does not exist. Try another one.\n")


init()