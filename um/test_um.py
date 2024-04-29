import pytest
from um import count


def test_phrase_1():
    assert count("um... this looks ok.") == 1


def test_phrase_2():
    assert count("umumum") == 0


def test_phrase_3():
    assert count("omgcs50um") == 0


def test_phrase_4():
    assert count("um um umum  ,um, ,um um,") == 5


def test_phrase_6():
    assert count("Um uM!") == 2

