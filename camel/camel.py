def Transform(my_input):
    SIZE = len(my_input)
    x = 0
    y = 0
    rc = " "

    while y != SIZE:
        if my_input[y].isupper():
            rc += my_input[x:y]
            rc += "_"
            x = y
        y += 1
    rc += my_input[x:SIZE]

    if rc == " ":
        rc = my_input
    else:
        rc = rc.strip().lower()

    return rc


def main():
    var = input("camelCase: ")
    print( Transform(var) )

main()
