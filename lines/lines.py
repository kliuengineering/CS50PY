# program input -> EXACTLY 1 CL arg -> name/path of a .py file
# program output -> # of lines of codes, exclude(comments, blank lines)
# sys.exit() if program input != .py or file path DNE

# useful method -> isspace(), from https://www.geeksforgeeks.org/how-to-remove-blank-lines-from-a-txt-file-in-python/


import sys


def CheckComplexity(file):
    rc = 0

    for line in file:
        if line.isspace():
            continue
        if line.strip()[0] == "#":
            continue
        rc += 1

    return rc


def main():
    arg = sys.argv
    if len(arg) < 2:
        sys.exit("Too few command-line arguments")
    elif len(arg) > 2:
        sys.exit("Too many command-line arguments")
    elif arg[1][-3:] != ".py":
        sys.exit("Not a Python file")
    else:
        pass
    FILE_PATH = arg[1]

    try:
        with open(FILE_PATH, "r") as file:
            complexity = CheckComplexity(file)
    except:
        sys.exit("File does not exist")

    print(complexity)


if __name__ == "__main__":
    main()
