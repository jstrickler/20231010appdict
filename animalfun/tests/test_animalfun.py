import pytest
from animalfun import Animalfun, sample_function

@pytest.fixture
def Animalfun_object():
    obj = Animalfun()
    return obj

def test_Animalfun_instance_has_sample_method(Animalfun_object):
    assert hasattr(Animalfun_object, "sample_method")

def test_animalfun_has_sample_function():
    assert sample_function() is None  # no return value
