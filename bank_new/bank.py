def main():
    print( f"${value( input("Say: ").strip() )}" )


# input(str), returns(int)
                # returns -> 0 if str == hello
                # returns -> 20 if str == h%
                # returns -> 100 otherwise
                # inputs(str) -> case insensitive
def value(greeting):
    rc = None

    if greeting.lower() == "hello":
        rc = 0
    elif greeting.lower()[0] == "h":
        rc = 20
    else:
        rc = 100

    return rc


if __name__ == "__main__":
    main()
