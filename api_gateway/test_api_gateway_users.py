from fastapi.testclient import TestClient
from api_gateway import app

client = TestClient(app)

def test_get_user_via_gateway():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Adam", "age": 25}
