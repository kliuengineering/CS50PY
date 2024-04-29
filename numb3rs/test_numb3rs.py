import sys
import re
import pytest
from numb3rs import validate


def test_validate_65535():
    assert validate("255.255.255.255") == True


def test_validate_overflow():
    assert validate("512.512.512.512") == False


def test_validate_partial_overflow():
    assert validate("1.2.3.1000") == False


def test_validate_invalid_char():
    assert validate("cat") == False


def test_validate_localhost():
    assert validate("127.0.0.1") == True


def test_validate_localhost_first_byte():
    try:
        assert validate("255.355.455.555") == False
    except AssertionError:
        sys.exit(1)


