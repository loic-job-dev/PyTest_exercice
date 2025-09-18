import pytest

from Diamond import diamond
from Diamond2 import diamond2


def test_diamond():
    expected = (
        "   a   \n"
        "  b b  \n"
        " c   c \n"
        "d     d\n"
        " c   c \n"
        "  b b  \n"
        "   a   \n"
    )
    assert diamond('d') == expected


def test_diamond2():
    expected = (
        "   a\n"
        "  b b\n"
        " c   c\n"
        "d     d\n"
        " c   c\n"
        "  b b\n"
        "   a\n"
    )
    assert diamond2('d') == expected