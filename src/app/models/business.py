import enum
from datetime import UTC, datetime

from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.app.core.database import Base


class Business(Base):
    __tablename__ = 'businesses'
    
    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    business_email = Column(String, unique=True, nullable=False)
    business_open = Column(DateTime, nullable=False)
    business_phone = Column(String, nullable=False)
    category = Column(String, nullable=False, default="pending")

    reservations = relationship("Reservation", back_populates="business")
