import random
import sys


def main():
    score = 0
    level = get_level()
    for i in range(10):
        score += Addition(level)
    # prints out the final score here...
    print(f"Score: {score}")


# prompts, reprompts the user for level and returns 1, 2, 3
def get_level():
    level = ""

    try:
        while not level.isnumeric() or int(level) < 1 or int(level) > 3:
            level = input("Level: ")

    except TypeError:
        sys.exit("Type error is seen, program exit...")
    except EOFError:
        sys.exit("\nEOF detected, program exit...")
    except KeyboardInterrupt:
        sys.exit("\nSIGINT detected, program exit...")

    return level


def Addition(level):
    x = generate_integer(level)
    y = generate_integer(level)
    z = x+y
    answer = -1
    counter = 3

    while z != answer and counter != 0:
        answer = input(f"{x} + {y} = ")
        counter -= 1

        if z == int(answer):
            return 1

        print("EEE")

    print(f"{x} + {y} = {z}")
    return 0


# returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3
def generate_integer(level):
    try:
        if level != "1" and level != "2" and level != "3":
            raise ValueError()
    except ValueError:
        sys.exit()

    level = int(level)

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
