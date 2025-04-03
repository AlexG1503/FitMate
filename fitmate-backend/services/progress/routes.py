from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.progress.conexion import get_db
from services.progress.schemas import ProgressCreate, ProgressResponse
from services.progress.crud import create_progress, get_user_progress

router = APIRouter(prefix="/progress", tags=["Progress"])

@router.post("/", response_model=ProgressResponse)
def add_progress(progress: ProgressCreate, db: Session = Depends(get_db)):
    return create_progress(db, progress)

@router.get("/{user_id}", response_model=list[ProgressResponse])
def get_progress(user_id: int, db: Session = Depends(get_db)):
    return get_user_progress(db, user_id)
