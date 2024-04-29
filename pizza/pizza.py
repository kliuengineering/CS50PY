# program input -> exactly 1 arg
    # if != 1 arg -> sys.exit
    # if DNE -> sys.exit
    # if not .csv -> sys.exit
# program output -> pretty table
    # format -> grid style


import csv
import sys
from tabulate import tabulate


# parsing the data into tabulate
def Parse(FILE_PATH):
    table = []

    with open(FILE_PATH, "r") as file:
        for line in file:
            table.append(line.split(","))

    headers = table[0]
    headers[-1] = headers[-1][:-1]

    table.pop(0)
    data = tabulate( table, headers, tablefmt = "grid" )

    if len(data) == 0:
        sys.exit("ERROR: data error...")
    return data


def PrintTable(data):
    print(data)


# validates the argv
def Validate(arg):
    FILE_PATH = None

    if len(arg) < 2:
        sys.exit("Too few command-line arguments")
    elif len(arg) > 2:
        sys.exit("Too many command-line arguments")
    elif arg[1][-4:] != ".csv":
        sys.exit("Not a CSV file")

    FILE_PATH = arg[1]

    try:
        with open(FILE_PATH, "r") as file:
            pass
    except TypeError:
        sys.exit("ERROR: file path is invalid...")
    except FileNotFoundError:
        sys.exit("File does not exist")

    return FILE_PATH


def main():
    arg = sys.argv
    FILE_PATH = Validate(arg)
    data = Parse(FILE_PATH)
    PrintTable(data)


if __name__ == "__main__":
    main()
