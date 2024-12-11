from datetime import UTC, datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Business(Base):
    __tablename__ = 'business'
    
    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    description = Column(String, nullable=False)
    
    reservations = relationship("Reservation", back_populates="business")