from fastapi.testclient import TestClient

# Import our app from main.py.
from main import app

# Instantiate the testing client with our app.
client = TestClient(app)

# Write tests using the same syntax as with the requests module.
def test_api_success():
    r = client.get("/items/34")
    assert r.status_code == 200
    assert r.json() == {"fetch": "Fetched 1 of 34"}

def test_api_failure():
    r = client.get("/items/a")
    assert r.status_code != 200
