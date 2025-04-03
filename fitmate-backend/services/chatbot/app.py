from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
import openai
import os
import uvicorn

app = FastAPI()

# 🔹 Ruta raíz para verificar que el servicio está activo
@app.get("/")
def home():
    return {"message": "¡Chatbot funcionando correctamente!"}

chatbot_router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@chatbot_router.post("/chat/")
def chat(request: ChatRequest):
    api_key = os.getenv("OPENAI_API_KEY")  # 🔹 Obtener la API Key desde variables de entorno

    if not api_key:  
        raise HTTPException(status_code=500, detail="API Key de OpenAI no configurada")

    openai_client = openai.OpenAI(api_key=api_key)  # 🔹 Usar OpenAI con su nueva API

    try:
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un asistente de gimnasio."},
                {"role": "user", "content": request.question}
            ],
            max_tokens=100,
            temperature=0.7
        )
        return {"response": response.choices[0].message.content}

    except openai.OpenAIError as e:  
        raise HTTPException(status_code=500, detail=f"Error con OpenAI: {str(e)}")

app.include_router(chatbot_router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)  # Cambia el puerto según corresponda









