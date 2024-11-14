from datetime import UTC, datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from app.core.database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow)
    phone = Column(Integer, unique=True, nullable=False)
    fullname = Column(String, nullable=False)

    #reservations = relationship("Reservation", back_populates="user")