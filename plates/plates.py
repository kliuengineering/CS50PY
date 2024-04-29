# [OK] maximum of 6 char
def max_char(plate):
    flag = False

    if len(plate) >= 2 and len(plate) <= 6:
        flag = True

    return flag


# [OK] no period, space, punctuation
def allowed_char(plate):
    flag = False

    if plate.isalnum():
        flag = True

    return flag


# [OK] start with at least 2 letters
def letter_head(plate):
    flag = False

    if plate[0].isalpha() and plate[1].isalpha():
        flag = True

    return flag


# numbers come in the end
def number_tail(plate):
    flag = False
    index = 0

    for i in range( len(plate) ):
        if plate[i].isnumeric():
            index = i
            break

    if plate[index:].isnumeric():
        flag = True

    return flag


# number XY -> X != 0
def number_zero(plate):
    flag = False
    index = 0

    for i in range( len(plate) ):
        if plate[i].isnumeric():
            index = i
            break

    if int( plate[index] ) != 0:
        flag = True

    return flag


# first number is not 0
def number_check(plate):
    flag = False

    if plate.isalpha():
        flag = True

    else:
        flag = number_tail(plate) and number_zero(plate)

    return flag


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    flag = False

    if( max_char(s) and allowed_char(s) and letter_head(s) and number_check(s) ):
        flag = True

    return flag


main()
