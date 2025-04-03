from fastapi.testclient import TestClient
from services.routines.app import app

client = TestClient(app)

def test_create_routine():
    response = client.post("/routines/", json={"name": "Cardio", "description": "Correr 30 min", "duration": 30})
    assert response.status_code == 200
    assert response.json()["name"] == "Cardio"

def test_get_routines():
    response = client.get("/routines/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
