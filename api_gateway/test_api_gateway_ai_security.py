from fastapi.testclient import TestClient
from api_gateway import app

client = TestClient(app)

def test_ai_no_query_param():
    response = client.get("/ai/analyze")
    assert response.status_code == 422  # brak wymaganych danych

def test_ai_long_query():
    long_query = "popraw kondycję " * 500
    response = client.get(f"/ai/analyze?query={long_query}")
    assert response.status_code == 200
    assert "kondycj" in response.json().get("response", "").lower()

def test_ai_suspicious_input():
    malicious_input = "DROP TABLE users; <?php echo 'hack'; ?>"
    response = client.get(f"/ai/analyze?query={malicious_input}")
    assert response.status_code == 200
    # AI ma prawo odpowiedzieć tekstem – nie sprawdzamy jego treści
