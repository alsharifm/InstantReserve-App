import enum
from datetime import UTC, datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import relationship

from app.core.database import Base

class Reservation(Base):
    __tablename__ = 'reservations'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # Primary key
    location = Column(String, nullable=False)
    time = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    business_id = Column(Integer, ForeignKey("businesses.id"), nullable=False)
    party_size = Column(Integer, nullable=False)
    reservationTime = Column(Integer, nullable=False)
    reservationDate = Column(DateTime, nullable=False)
    date_time = Column(DateTime, nullable=False)

    
    user = relationship("User", back_populates="reservations")
    business = relationship("Business", back_populates="reservations")