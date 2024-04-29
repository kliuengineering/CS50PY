array_students = []
array_students_sorted = []


def Parse():
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            student = {"name":name, "house":house}
            array_students.append(student)


def GetHouse(student):
    return student["house"]


# sort
def Sort():
    for student in sorted( array_students, key=GetHouse ):
        array_students_sorted.append( {"name":student["name"], "house":student["house"]} )


def Print(array):
    for itr in array:
        print(itr)


def main():
    Parse()
    Print(array_students)
    print("")
    Sort()
    Print(array_students_sorted)


if __name__ == "__main__":
    main()
