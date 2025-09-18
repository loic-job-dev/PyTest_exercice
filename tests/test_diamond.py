import pytest

from Diamond import diamond

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
