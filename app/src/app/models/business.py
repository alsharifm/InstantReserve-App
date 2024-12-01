import enum
from datetime import UTC, datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine
from sqlalchemy.orm import relationship

from app.core.database import Base

class Business(Base):
    __tablename__ = 'businesses'
    
    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=False)
    business_email = Column(String, nullable=False)
    businessOpen = Column(Integer, nullable=False)
    business_phone = Column(Integer, nullable=False)
    category = Column(String, nullable=False, default="pending")


 #   reservation = relationship("Reservation", back_populates="business")

