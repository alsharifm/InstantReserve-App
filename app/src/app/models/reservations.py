from datetime import UTC, datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from app.core.database import Base

class Reservation(Base):
    __tablename__ = 'reservations'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    time = Column(Integer, nullable=False)
    date = Column(Integer, nullable=False)
    
    business_id = relationship("Business", back_populates="reservations")
    reservations = relationship("Reservation", back_populates="user")