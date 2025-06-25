import pytest
import datetime
from dateutil.relativedelta import relativedelta

from src.cat_pkg.assign_2 import app as cat_app
from src.cat_pkg import cat_code as cc

@pytest.fixture()
def app():
    cat_app.config.update({
        "TESTING": True,
    })
    yield cat_app    

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def http_clowder():
    clowder = cc.Clowder("Test_Clowder")
    return clowder

@pytest.fixture
def http_cat():
    ten_yrs_old = str(datetime.date.today() - relativedelta(years=10))
    cat = cc.Cat("Big_Tom",dob=ten_yrs_old,male=True,intact=True)
    return cat

def test_build_clowder(http_clowder, http_cat):
    http_clowder.cat_moves_in(http_cat)
    assert len(http_clowder.clowder) == 1

def test_get_empty_clowder(client):
    response = client.get('/clowders')
    assert response.status_code == 200 and response.json == {'Clowders' : []}

def test_post_clowder(client,http_clowder):
    clowder_data = http_clowder.get_clowder_dict()
    response = client.post('/clowders', json = clowder_data)
    assert response.status_code == 201 and response.json == {'Clowder_Name' : "Test_Clowder", "Clowder_Size" : 1}

def test_get_named_clowder(client,http_clowder):
    name = http_clowder.get_clowder_name()
    response = client.get('/clowders/'+name)
    assert response.status_code == 200

def test_put_new_arrival_date(client,http_clowder,http_cat):
    cat_name = http_cat.get_name()
    clowder_name = http_clowder.get_clowder_name()
    response = (client.put('/clowders/'+clowder_name+'/'+cat_name, json = {"New_Date" :'1/1/2001'}))
    assert response.status_code == 202 

def test_del_cat(client, http_clowder,http_cat):
    clowder_name = http_clowder.get_clowder_name()
    cat_name = http_cat.get_name()
    response = (client.delete('/clowders/' + clowder_name+'/'+cat_name))
    assert response.status_code == 203
    
def test_del_clowder(client, http_clowder):
    clowder_name = http_clowder.get_clowder_name()
    response = (client.delete('/clowders/' + clowder_name))
    assert response.status_code == 203

def test_del_cat(client, http_clowder,http_cat):
    clowder_name = http_clowder.get_clowder_name()
    cat_name = http_cat.get_name()
    response = (client.delete('/clowders/' + clowder_name+'/'+cat_name))
    assert response.status_code == 203
