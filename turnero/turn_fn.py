departments = {
    "d": "Drugstore",
    "p": "Perfumery",
    "c": "Cosmetics"
}


def generate_turn_drugstore():
    for t in range(1, 100):
        yield f"D-{t}"


def generate_turn_perfumery():
    for t in range(1, 100):
        yield f"P-{t}"


def generate_turn_cosmetics():
    for t in range(1, 100):
        yield f"C-{t}"


d = generate_turn_drugstore()
p = generate_turn_perfumery()
c = generate_turn_cosmetics()


def decorate_turn(dep):
    print("\n" + "*" * 23)
    if dep == "d":
        print(f"Your number is: {next(d)}")
    elif dep == "p":
        print(f"Your number is: {next(p)}")
    else:
        print(f"Your number is: {next(c)}")

    print("Wait for it!")
    print("*"*23 + "\n")


