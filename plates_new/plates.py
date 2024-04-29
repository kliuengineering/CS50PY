def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# input(str), output(bool),
def is_valid(s):
    flag = True

    if not( len(s) > 1 and len(s) < 7):
        flag = False

    if not( s[0].isalpha() or s[1].isalpha() ):
        flag = False

    index = -1
    for i in range( len(s) ):
        if s[i].isnumeric():
            index = i
            break
    if index > -1 and not s[index:].isnumeric():
        flag = False

    if not s.isalnum():
        flag = False

    comparison = []
    for itr in s:
        if itr.isnumeric():
            comparison.append(itr)
    if len(comparison) > 0 and comparison[0] == "0":
        flag = False

    return flag


if __name__ == "__main__":
    main()
