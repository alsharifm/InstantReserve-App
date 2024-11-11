# models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    ##Will code work to show multiple reservations under the same user?
    reservations = relationship("Reservation", back_populates="user")


class Reservation(Base):
    __tablename__ = 'reservations'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    location = Column(String, nullable=False)
    time = Column(DateTime, nullable=False)
    party_size = Column(Integer, nullable=False)
    status = Column(String, nullable=False, default="pending")

    user = relationship("User", back_populates="reservations")
    business = relationship("Business", back_populates="reservations")

##Will code work to show multiple reservations under the same business?
class Business(Base):
    __tablename__ = 'businesses'
    
    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(Integer, ForeignKey('users.id'))
    location = Column(String, nullable=False)
    business_email = Column(DateTime, nullable=False)
    business_phone = Column(Integer, nullable=False)
    category = Column(String, nullable=False, default="pending")

    reservations = relationship("Reservation", back_populates="business")
