from fastapi.testclient import TestClient
from health_service import app

client = TestClient(app)

def test_get_existing_health_data():
    response = client.get("/health/1")
    assert response.status_code == 200
    assert response.json() == {"steps": 10000, "calories": 500}

def test_get_nonexistent_health_data():
    response = client.get("/health/999")
    assert response.status_code == 200
    assert response.json() == {"error": "Health data not found"}

