# utility function 1
def is_empty(array):
    if len(array) == 0:
        return True
    else:
        return False


# quick sort practice
def QuickSort( array_grocery ):
    if is_empty( array_grocery ):
        return array_grocery

    elif len(array_grocery) == 1:
        return array_grocery

    else:
        pivot = array_grocery.pop()

    partition_left = []
    partition_right = []

    for itr in array_grocery:
        if itr > pivot:
            partition_right.append(itr)
        else:
            partition_left.append(itr)

    return QuickSort( partition_left ) + [ pivot ] + QuickSort( partition_right )


# handles array duplicates, and put into a dict
def HandleDupes( array_grocery ):
    dict_grocery = {}

    for itr in array_grocery:
        if itr not in dict_grocery:
            dict_grocery[itr] = 1
        else:
            dict_grocery[itr] += 1

    return dict_grocery


# utility function 2
def UpperCase( array_grocery ):
    rc = []

    for itr in array_grocery:
        rc.append( itr.upper() )

    return rc


# utility function 3
def Print( dict_grocery ):
    for key in dict_grocery:
        print(f"{dict_grocery[key]} {key}")


def main():
    array_grocery = []
    dict_grocery = {}
    is_running = True

    while is_running:
        try:
            array_grocery.append( input() )
            array_grocery = UpperCase(array_grocery)
            array_grocery = QuickSort(array_grocery)
            dict_grocery = HandleDupes(array_grocery)

        except EOFError:
            Print( dict_grocery )
            is_running = False


main()
