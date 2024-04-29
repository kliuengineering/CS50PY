def main():
    is_running = True
    while is_running:
        fraction = input("Fraction: ")
        percentage = convert(fraction)
        print(percentage)
        break


# input(str = "X/Y"), output( round(fraction=percentage) )
# raise ValueError -> X != int or Y != int, X > Y
# raise ZeroDivisionError -> y == 0
def convert(fraction):

    try:
        x, y = fraction.strip().split("/")
    except ValueError:
        return -1

    if int(y) == 0:
        raise ZeroDivisionError

    if int(x) > int(y):
        raise ValueError

    if int(x) < 0 or int(y) < 0:
        raise ValueError

    rc = gauge( int( 100*round(float(x)/float(y), 2) ) )


    return rc


# input(int), output(str)
# output -> "E" if int < 2
# output -> "F" if int > 98
# else output -> int%
def gauge(percentage):
    rc = None
    if percentage < 2:
        rc = "E"
    elif percentage > 98:
        rc = "F"
    else:
        rc = str(percentage) + "%"
    return rc


if __name__ == "__main__":
    main()
