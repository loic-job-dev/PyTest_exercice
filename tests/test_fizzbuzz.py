import pytest

from FizzBuzz import fizzbuzz

def test_fizzbuzz_fizz():
    assert fizzbuzz(3) == "1\n2\nfizz\n"
    assert fizzbuzz(5) == "1\n2\nfizz\n4\n5\n"

