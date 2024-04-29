def main():
    message = "This is CS50"
    yell(message)
    yell_2([message])
    yell_3(message)
    yell_4(message)
    yell_5(message)


def yell(phrase):
    print(phrase.upper())


# not a pythony way
def yell_2(phrase):
    uppercased = []
    for word in phrase:
        uppercased.append(word.upper())
    print(*uppercased)


def yell_3(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


# map function to a sequence, functional programming
def yell_4(*words):
    uppercased = map(str.upper, words)   # maps from one function to another
    print(*uppercased)


# list comprehension
def yell_5(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
