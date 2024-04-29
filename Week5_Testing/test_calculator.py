from calculator import square


def main():
    test_square()


def test_square():
    try:
        assert square(3) == 9

    except AssertionError:
        print("3 squared is not 9")


if __name__ == "__main__":
    main()
