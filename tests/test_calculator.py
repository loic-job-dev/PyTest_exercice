from Calculator import add

#To launch tests, execute 'pytest' command

def test_add():
    assert add(1, 2) == 3
    assert add(-2, -3) == -5
    assert add(3, -1) == 2

