from pydantic import BaseModel
from datetime import datetime

class ProgressBase(BaseModel):
    user_id: int
    weight: float
    body_fat: float
    muscle_mass: float
    body_age: int | None = None
    waist: float | None = None
    chest: float | None = None
    thighs: float | None = None

class ProgressCreate(ProgressBase):
    pass

class ProgressResponse(ProgressBase):
    id: int
    recorded_at: datetime

    class Config:
        from_attributes = True
