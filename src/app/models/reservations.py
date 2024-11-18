import enum
from datetime import UTC, datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey
from src.app.core.database import Base
from sqlalchemy.orm import relationship

from src.app.core.database import Base

class Reservation(Base):
    __tablename__ = 'reservations'
    
    id = Column(Integer, primary_key=True, index=True)
    time = Column(Integer, nullable=False)
    date = Column(Integer, nullable=False)
    #user_id = Column(Integer, ForeignKey("users.id"))
    #business_id = Column(Integer, ForeignKey("business.id"))
    party_size = Column(Integer, nullable = False)
    
    #user = relationship("User", back_populates="reservation")
    #business = relationship("Business", back_populates="reservations")