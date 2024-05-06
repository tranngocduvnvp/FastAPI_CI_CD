# File: test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_endpoint():
    response = client.get("/add?x=5&y=3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}

    response = client.get("/add?x=-2&y=2")
    assert response.status_code == 200
    assert response.json() == {"result": 0}

    response = client.get("/add?x=100&y=-99")
    assert response.status_code == 200
    assert response.json() == {"result": 1}

def test_add_endpoint_invalid_input():
    response = client.get("/add?x=abc&y=def")
    assert response.status_code == 422

    response = client.get("/add?x=1")
    assert response.status_code == 422

    response = client.get("/add")
    assert response.status_code == 422


