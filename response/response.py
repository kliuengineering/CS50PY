from validator_collection import validators


def main():
    addr = input("What is your E-mail: ")
    print( Validate(addr) , end="" )


def Validate(addr):
    flag = None
    try:
        flag = validators.email(addr)
        flag = "Valid"
    except:
        flag = "Invalid"

    return flag

# def Validate(addr):
#     flag = None
#     try:
#         validators.email(addr)
#         flag = "Valid"
#     except validators.utils.ValidationError:
#         flag = "Invalid"

#     return flag


if __name__ == "__main__":
    main()

    
