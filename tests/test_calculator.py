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