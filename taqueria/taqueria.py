Menu = {
    "Baja Taco": 21.25,
    "Burrito": 27.00,
    "Bowl": 27.00,
    "Nachos": 27.00,
    "Quesadilla": 21.25,
    "Super Burrito": 21.25,
    "Super Quesadilla": 9.50,
    "Taco": 14.00,
    "Tortilla Salad": 14.00
}

# order placing
# loop ... until control-d
# running total cost after each prompt
# display - float, $, 2 decimals
# user input - case insensitive
# ignore all invalid input

def Stage(result):
    result = round(result, 2)
    return result


def Search(item):
    result = None
    item = item.strip().lower().title()

    try:
        result = Menu[item]
        result = Stage(result)

    except KeyError:
        pass

    return result


def main():
    is_running = True
    while is_running:
        try:
            item = input("Item: ")
            print( f"${format( Search(item), ".2f" )}" )

        except TypeError:
            continue

        except EOFError:
            is_running = False

main()
