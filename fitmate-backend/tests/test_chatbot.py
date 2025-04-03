from fastapi.testclient import TestClient
from services.chatbot.app import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "¡Chatbot funcionando correctamente!"}

def test_chat_no_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    response = client.post("/chat/", json={"question": "¿Cuál es el mejor ejercicio para espalda?"})
    assert response.status_code == 500
    assert response.json()["detail"] == "API Key de OpenAI no configurada"
