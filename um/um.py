import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    counter = 0
    s = s.strip()

    if len(s) < 2:
        pass
    elif len(s) == 2:
        if s == "um":
            counter += 1
    elif len(s) == 3:
        if s == "um[^w]":
            counter += 1
    else:
        counter += Search(s)

    return counter


def Search(string):
    counter = 0

    pattern = r"(?<!\w)um(?!\w)"
    matches = re.findall(pattern, string, re.IGNORECASE)
    counter += len(matches)

    return counter


if __name__ == "__main__":
    main()
