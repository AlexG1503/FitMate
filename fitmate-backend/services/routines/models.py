from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Routine(Base):
    __tablename__ = "routines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    duration = Column(Integer, nullable=False)  # Duración en minutos
