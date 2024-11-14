from datetime import UTC, datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from app.core.database import Base

class Business(Base):
    __tablename__ = 'businesses'
    
    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(Integer, ForeignKey('users.id'))
    address = Column(String, nullable=False)
    business_email = Column(String, nullable=False)
    businessOpen = Column(Integer, nullable=False)
    business_phone = Column(Integer, nullable=False)
    category = Column(String, nullable=False, default="pending")

    reservations = relationship("Reservation", back_populates="business")