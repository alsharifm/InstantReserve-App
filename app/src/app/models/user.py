from datetime import UTC

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    fullname = Column(String, nullable=False)
    verification_code = Column(String, nullable=True)
    
    reservation = relationship("Reservation", back_populates="user")