import pytest

from Diamond import diamond

def test_diamond():
    assert diamond('d') == "   d           "