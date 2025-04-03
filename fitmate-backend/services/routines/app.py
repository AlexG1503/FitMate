from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from models import Routine
import uvicorn
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

# Ruta para registrar una rutina
@app.post("/routines/")
def create_routine(name: str, description: str, duration: int, db: Session = Depends(get_db)):
    new_routine = Routine(name=name, description=description, duration=duration)
    db.add(new_routine)
    db.commit()
    db.refresh(new_routine)
    return new_routine

# Ruta para obtener todas las rutinas
@app.get("/routines/")
def get_routines(db: Session = Depends(get_db)):
    return db.query(Routine).all()

# Ruta para obtener una rutina específica
@app.get("/routines/{routine_id}")
def get_routine(routine_id: int, db: Session = Depends(get_db)):
    routine = db.query(Routine).filter(Routine.id == routine_id).first()
    if not routine:
        raise HTTPException(status_code=404, detail="Rutina no encontrada")
    return routine

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
