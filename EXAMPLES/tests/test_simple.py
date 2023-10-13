# from some_module import thing_to_be_tested
import pytest

def test_two_plus_two_equals_four():  # tests should begin with "test" (or will not be found automatically)
    assert 2 + 2 == 4  # if assert statement succeeds, the test passes

def test_identity():
    assert True

def open_file(file_path):
    x = open(file_path)
    return x.read()

def test_open_missing_file_fails():
    with pytest.raises(FileNotFoundError):
        data = open_file('wombats_are_our_friends.txt')

def add_point_two(value):
    return .2 + value

def test_decimals():
    assert add_point_two(.1) == pytest.approx(.3)













