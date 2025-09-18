import pytest

from FizzBuzz import fizzbuzz

def test_fizzbuzz_fizz():
    assert fizzbuzz(3) == "1\n2\nfizz\n"
    #assert fizzbuzz(5) == "1\n2\nfizz\n4\n5\n"

def test_fizzbuzz_buzz():
    assert fizzbuzz(5) == "1\n2\nfizz\n4\nbuzz\n"
    assert fizzbuzz(15) == "1\n2\nfizz\n4\nbuzz\nfizz\n7\n8\nfizz\nbuzz\n11\nfizz\n13\n14\nfizzbuzz\n"