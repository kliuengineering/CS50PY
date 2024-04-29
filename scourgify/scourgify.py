# input file -> name, house
# output file -> first, last, house


import csv
import sys


def Input(PATH_NAME):
    data = []

    try:
        with open(PATH_NAME, "r") as FILE:
            reader = csv.DictReader(FILE)
            for row in reader:
                data.append( { "name":row["name"], "house":row["house"] } )
    except:
        sys.exit("Error: issue parsing data")

    fname = []
    lname = []
    house = []
    cleaned_data = []

    for itr in data:
        # print(itr)
        last, first = itr["name"].split(",")
        fname.append( first.strip() )
        lname.append( last.strip() )
        house.append( itr["house"].strip() )

    cleaned_data.append(["first,last,house\n"])
    for i in range(len(fname)):
        cleaned_data.append(
            [
                fname[i] + "," +
                lname[i] + "," +
                house[i] + "\n"
            ]
        )

    return cleaned_data


def Output(FILE_PATH, cleaned_data):

    try:
        with open(FILE_PATH, "x") as FILE:
            pass
    except ValueError:
        sys.exit("ERROR: file creation")
    except FileExistsError:
        pass

    try:
        with open(FILE_PATH, "w") as FILE:
            for itr in cleaned_data:
                FILE.write(itr[0])
    except ValueError:
        sys.exit("ERROR: file write")


def Validate(argv):

    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 3:
        sys.exit("Too many command-line arguments")
    elif argv[1][-4:] != ".csv" or argv[2][-4:] !=".csv":
        sys.exit("Not a CSV file")

    PATH_NAME_INPUT = argv[1]
    PATH_NAME_OUTPUT = argv[2]

    try:
        with open(PATH_NAME_INPUT, "r"):
            pass
    except TypeError:
        sys.exit("ERROR: file path is invalid...")
    except FileNotFoundError:
        sys.exit(f"Could not read {PATH_NAME}")

    return PATH_NAME_INPUT, PATH_NAME_OUTPUT


def main():
    argv = sys.argv
    PATH_NAME_INPUT, PATH_NAME_OUTPUT = Validate(argv)
    data = Input(PATH_NAME_INPUT)
    # print(data)
    Output(PATH_NAME_OUTPUT, data)


if __name__ == "__main__":
    main()
