students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


# example of list comprehension
def list_comprehension() -> None:
    gryffindors = [
        student["name"] for student in students if student["house"] == "Gryffindor"
    ]
    print(gryffindors)


# example of filtering
def filter_gryffindor(s) -> bool:
    if s["house"] == "Gryffindor":
        return True
    else:
        return False


# example of lambda
def lambda_example(s):
    gryffindors = filter(filter_gryffindor, students)
    for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
        print(gryffindor["name"])


def main():
    list_comprehension()
    print( *filter(filter_gryffindor, students) )
    lambda_example(students)


if __name__ == "__main__":
    main()
