from fastapi.testclient import TestClient

from source.query.main import app

client = TestClient(app)

def test_get_path():
    output = client.get("/items/42") 
    assert output.status_code == 200
    assert output.json() == {"fetch": "Fetched 1 of 42... Bye!"}

def test_get_path_query():
    output = client.get("/items/30?count=10&msg=GoodBye!")
    assert output.status_code == 200
    assert output.json() == {"fetch": "Fetched 10 of 30... GoodBye!"}

def test_get_malformed():
    output = client.get("/items")
    assert output.status_code != 200

