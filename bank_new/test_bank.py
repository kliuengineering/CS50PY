import pytest
import sys
import random
from bank import value


def test_hello():
    assert value("hello") == 0


def test_h():
    assert value("hi") == 20


def test_UpperLower():
    assert value("HEllo") == 0


def test_random():
    try:
        assert value( random.randint(-999, 999) ) == 100
    except AttributeError:
        return -1


def test_space():
    try:
        assert value(" ")
    except IndexError:
        return -1
