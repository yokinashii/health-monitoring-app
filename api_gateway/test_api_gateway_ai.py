from fastapi.testclient import TestClient
from api_gateway import app

client = TestClient(app)

def test_ai_analyze_via_gateway():
    response = client.get("/ai/analyze?query=co to jest ketoza")
    assert response.status_code == 200
    assert "ketoza" in response.json().get("response", "").lower()
