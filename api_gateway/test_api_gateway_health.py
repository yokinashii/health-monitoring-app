from fastapi.testclient import TestClient
from api_gateway import app

client = TestClient(app)

def test_get_health_via_gateway():
    response = client.get("/health/1")
    assert response.status_code == 200
    assert response.json() == {"steps": 10000, "calories": 500}
