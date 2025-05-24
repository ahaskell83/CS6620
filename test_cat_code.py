import pytest
import datetime
from dateutil.relativedelta import relativedelta
from cat_code import Cat, Clowder

@pytest.fixture
def cat():
    ten_yrs_old = str(datetime.date.today() - relativedelta(years=10))
    cat = Cat("Big Tom",dob=ten_yrs_old,male=True,intact=True)
    return cat

@pytest.fixture
def clowder():
    clowder = Clowder("Test Clowder")
    return clowder

@pytest.fixture
def cat_family():
    names = ["Mom","Dad","Fluffy","Shaggy","Sleek"]
    dobs = ['1/1/2018', '1/1/2020', '1/1/2025', '1/1/2025', '1/1/2025']
    male = [False, True, True, True, False]
    intact = [True,True, True, True, True]
    cats = []
    for i in range (5):
        cats.append(Cat(names[i],dobs[i],male[i],intact[i]))
    return cats

@pytest.fixture
def breeding_cats():
    cat_found_family = [Cat('Karen','1/1/2019',False,True),Cat('Kelsie','1/1/2020',False,True),Cat('George','1/1/2020',True,True)]
    return cat_found_family

def test_cat_creation(cat):
    assert cat.name == "Big Tom"
    assert cat.age_in_yrs == 10

def test_add_single_cat(clowder, cat):
    clowder.cat_moves_in(cat)
    assert len(clowder.clowder) == 1
    assert clowder.get_clowder_names() == ["Big Tom"]

def test_add_family_of_cats(clowder, cat_family):
    clowder.cat_family_moves_in(cat_family)
    assert len(clowder.clowder) == 6

def test_add_family_with_arrival_date(clowder, breeding_cats):
    clowder.cat_family_moves_in(breeding_cats,arrival_date = '11/1/2024')
    assert len(clowder.clowder) == 9

