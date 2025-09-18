import pytest

from Calculator import add
from Calculator import sub

#To launch tests, execute 'pytest' command

def test_add():
    assert add(1, 2) == 3
    assert add(-2, -3) == -5
    assert add(3, -1) == 2

def test_sub():
    assert sub(2, 1) == 1
    assert sub(-2, -3) == 1
    assert sub(3, -1) == 4

@pytest.fixture
def int_list():
    return [1, 2, 3]

def test_add_with_fixture(int_list):
    assert add(int_list[0], int_list[1]) == int_list[2]
    assert add(int_list[0], int_list[2]) == 4