from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from services.progress.conexion import Base
from datetime import datetime

class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    weight = Column(Float, nullable=False)
    body_fat = Column(Float, nullable=False)
    muscle_mass = Column(Float, nullable=False)
    body_age = Column(Integer, nullable=True)
    waist = Column(Float, nullable=True)
    chest = Column(Float, nullable=True)
    thighs = Column(Float, nullable=True)
    recorded_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="progress")
