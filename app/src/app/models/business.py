from datetime import UTC, datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from app.core.database import Base
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine

class BusinessReservationLink(SQLModel, table=True):
    reservation_id: int | None = Field(default=None, foreign_key="reservation.id", primary_key=True)
    business_id: int | None = Field(default=None, foreign_key="business.id", primary_key=True)

class Business(Base):
    __tablename__ = 'businesses'
    
    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=False)
    business_email = Column(String, nullable=False)
    businessOpen = Column(Integer, nullable=False)
    business_phone = Column(Integer, nullable=False)
    category = Column(String, nullable=False, default="pending")

    #reservations = relationship(back_populates="business", link_model = BusinessReservationLink)

