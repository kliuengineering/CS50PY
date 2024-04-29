def main():
    print( f"Output: {shorten( input("Input: ") )}" )


def shorten(word): # => returns a string
    array = []

    for itr in word:
        if itr.lower() != "a" and itr.lower() != "e" and itr.lower() != "i" and itr.lower() != "o" and itr.lower() != "u":
            array.append(itr)

    rc = "".join(array)
    return rc


if __name__ == "__main__":
    main()
