import pytest
from cat_code import Cat, Clowder

@pytest.fixture
def cat():
    cat = Cat("Big Tom",dob='5/24/2015',male=True,intact=True)
    return cat
    
@pytest.fixture
def clowder():
    clowder = Clowder()
    return clowder

def test_cat_creation(cat):
    assert cat.name == "Big Tom"
    assert cat.age_in_yrs == 10

def test_single_cat(clowder, cat):
    clowder.cat_moves_in(cat)
    assert len(clowder.clowder) == 1
