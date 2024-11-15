from datetime import UTC, datetime

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.app.core.database import Base


class Reservation(Base):
    __tablename__ = 'reservations'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date_time = Column(DateTime, nullable=False)
    business_id = Column(Integer, ForeignKey('businesses.id'), nullable=False)
    
    user = relationship("User", back_populates="reservations")
    business = relationship("Business", back_populates="reservations")