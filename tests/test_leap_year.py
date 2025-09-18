from LeapYear import is_leap_year

def test_is_leap_year():
    assert is_leap_year(2000) == True
    assert is_leap_year(1800) == False
    assert is_leap_year(2008) == True
    assert is_leap_year(2018) == False