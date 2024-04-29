import sys
import pytest
from plates import is_valid


def test_num_leading():
    assert is_valid("50CS") == False
    assert is_valid("50") == False


def test_num_in_between():
    assert is_valid("CS50P") == False


def test_alpha_numeric():
    assert is_valid("CS50!") == False


def test_space():
    assert is_valid("CS 50") == False


def test_max():
    assert is_valid("CSPython") == False


def test_min():
    assert is_valid("C") == False


def test_leading_zero():
    assert is_valid("CS050") == False

