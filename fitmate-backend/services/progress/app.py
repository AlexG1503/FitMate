from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from services.progress.conexion import SessionLocal, init_db
from services.progress.models import Progress
import uvicorn
from services.progress.schemas import ProgressCreate, ProgressResponse
from services.progress.crud import create_progress, get_progress_by_user
from contextlib import asynccontextmanager

# Lifespan event handler en lugar de @app.on_event("startup")
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()  # Inicializar la DB al iniciar
    yield  # Permite continuar con la ejecución normal de la app

app = FastAPI(lifespan=lifespan)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para registrar el progreso del usuario
@app.post("/progress/", response_model=ProgressResponse)
def register_progress(progress_data: ProgressCreate, db: Session = Depends(get_db)):
    return create_progress(db, progress_data)

# Ruta para obtener el progreso de un usuario
@app.get("/progress/{user_id}", response_model=list[ProgressResponse])
def get_user_progress(user_id: int, db: Session = Depends(get_db)):
    return get_progress_by_user(db, user_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8004)
