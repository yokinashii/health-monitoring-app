from fastapi.testclient import TestClient
from users_service import app

client = TestClient(app)

def test_get_existing_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Adam", "age": 25}

def test_get_nonexistent_user():
    response = client.get("/users/999")
    assert response.status_code == 200
    assert response.json() == {"error": "User not found"}
