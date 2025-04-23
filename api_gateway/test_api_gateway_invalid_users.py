from fastapi.testclient import TestClient
from api_gateway import app

client = TestClient(app)

def test_non_existing_user():
    response = client.get("/users/9999")
    assert response.status_code == 200
    assert response.json() == {"error": "User not found"}
