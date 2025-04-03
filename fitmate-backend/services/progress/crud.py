from sqlalchemy.orm import Session
from services.progress.models import Progress
from services.progress.schemas import ProgressCreate

def create_progress(db: Session, progress_data: ProgressCreate):
    new_progress = Progress(**progress_data.dict())
    db.add(new_progress)
    db.commit()
    db.refresh(new_progress)
    return new_progress

def get_progress_by_user(db: Session, user_id: int):
    return db.query(Progress).filter(Progress.user_id == user_id).all()
