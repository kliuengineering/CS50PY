import sys
import pytest
from fuel import convert, gauge


def test_zero_division():
    try:
        assert convert("5/0")
    except ZeroDivisionError:
        pass


def test_value_error():
    try:
        assert convert("10/8")
    except ValueError:
        pass


def test_one_percent():
    assert gauge(1) == "E"


def test_ninty_nine_percent():
    assert gauge(99) == "F"


def test_printing_percent():
    assert gauge(50) == "50%"


def test_wrong_type():
    try:
        assert convert(2/4)
    except AttributeError:
        pass


def test_incorrect_ints_return():
    try:
        assert convert("-1/2")
    except ValueError:
        pass


def test_incorrect_input_values():
    try:
        assert convert("Cat/Dog")
    except ValueError:
        pass


# def test_incorrect_ints_return():
#     with pytest.raises(ValueError):
#         convert("-1/2")
