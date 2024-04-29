def example_set():
    array = [1, 1, 2, 2, 3, 4, 5]
    myset = set(array)
    myset.add(1)
    print(myset)


def example_arrow_notation() -> (int, str):
    return 3, "5"


def example_unpacking():
    coins = [[100, 50, 25], [66, 33, 22, 11]]
    print( *coins )


def PrintDict(Dollar, Quarter, Dime):
    print(Dollar, Quarter, Dime)
def example_unpacking_2():
    coins = {"Dollar":100, "Quarter":25, "Dime":10}
    PrintDict( **coins )


def example_unpacking_3(*args, **kwargs):
    print("Argument: ", args)
    print("Named Args: ", kwargs)


def main():
    print( example_arrow_notation() )
    example_unpacking()
    example_unpacking_2()
    example_unpacking_3(1, 2, 3, 4, 5)
    example_unpacking_3(1, 2, 3, 4, 5, dollar=100, quarter=25, dime=10)


if __name__ == "__main__":
    main()
