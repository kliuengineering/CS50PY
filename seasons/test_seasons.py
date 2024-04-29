from seasons import Start, Validate


def test_incorrect_input():
    try:
        assert Start("meow")
    except SystemExit:
        pass


def test_incorrect_input2():
    try:
        assert Start("19200101")
    except SystemExit:
        pass


def test_incorrect_input3():
    try:
        assert Start(20000101)
    except TypeError:
        pass


def test_validation():
    assert Validate("19000101") == -1


def test_validation2():
    assert Validate("1900-01-01") == "1900-01-01"
