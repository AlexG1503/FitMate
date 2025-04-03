from fastapi.testclient import TestClient
from services.progress.app import app

client = TestClient(app)

def test_register_progress():
    response = client.post("/progress/", json={"user_id": 1, "exercise": "Bench Press", "reps": 10, "weight": 50})
    assert response.status_code == 200
    assert response.json()["exercise"] == "Bench Press"

def test_get_progress():
    response = client.get("/progress/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
