# models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow)
    phone = Column(Integer, unique=True, nullable=False)
    fullname = Column(String, nullable=False)
    ##Will code work to show multiple reservations under the same user?
    reservations = relationship("Reservation", back_populates="user")


class Reservation(Base):
    __tablename__ = 'reservations'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    time = Column(Integer, nullable=False)
    date = Column(Integer, nullable=False)
    
    business_id = relationship("Business", back_populates="reservations")

##Will code work to show multiple reservations under the same business?
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
