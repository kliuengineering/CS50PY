import pytest
from working import convert


# implement 3+ functions to test convert() thoroughly


def test_correct_input():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_correct_input_2():
    assert convert("9:59 AM to 5:59 PM") == "09:59 to 17:59"


def test_incorrect_input():
    try:
        assert convert("9 AM 5 PM")
    except ValueError:
        pass

def test_incorrect_input():
    try:
        assert convert("9AM to 5PM")
    except ValueError:
        pass


def test_incorrect_input_2():
    try:
        assert convert("MEOW")
    except ValueError:
        pass


def test_incorrect_input_3():
    try:
        assert convert("9:80 AM to 5:80 PM")
    except ValueError:
        pass


def test_incorrect_input_4():
    try:
        assert convert("14 to 16")
    except ValueError:
        pass


def test_incorrect_input_5():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")


def test_incorrect_input_6():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5 PM")





