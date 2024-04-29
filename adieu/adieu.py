array = []
comma = 0


def Interface():

    array.append( input("Name: ") )


def Calculate():
    global comma
    comma = len( array ) - 1


def Print():
    global comma
    string_1 = "Adieu, adieu, to "
    string_2 = ""

    for i in range( len(array) - 1 ):
        string_2 += array[i]
        if comma > 0:
            string_2 += ", "
            comma -= 1

    if len(array) == 0:
        return

    elif len(array) == 1:
        string_3 = string_1 + array[0]

    elif len(array) == 2:
        string_3 = string_1 + array[0] + " and " + array[1]

    else:
        string_3 = string_1 + string_2 + "and " + array[-1]

    print(string_3)


def main():

    is_running = True

    while is_running:
        try:
            Interface()

        except EOFError:
            Calculate()
            Print()
            is_running = False

if __name__ == "__main__":
    main()
