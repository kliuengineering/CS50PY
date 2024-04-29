import pytest
import sys
from twttr import shorten


def test_upper():
    assert shorten("A E I O U") == "    "


def test_empty():
    assert shorten("   ") == "   "


def test_lower():
    assert shorten("a e i o u") == "    "


# def test_number():
#     with pytest.raises(TypeError):
#         shorten(55)
#     with pytest.raises(TypeError):
#         shorten(0x09)


def test_escape():
    assert shorten("\n") == "\n"


def test_puncuation():
    assert shorten("Hi, Kevin") == "H, Kvn"


def test_number():
     assert shorten("0x66") == "0x66"

