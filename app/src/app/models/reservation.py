import enum
from datetime import UTC, datetime


from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base

class Reservation(Base):
    __tablename__ = "reservations"

    
    id = Column(Integer, primary_key=True, index=True)
    creation_date = Column(DateTime, default=datetime.now(UTC))
    reservation_time = Column(Integer, nullable=False)
    party_size = Column(Integer, nullable = False)

    user_id = Column(Integer, ForeignKey("users.id"))
    business_id = Column(Integer, ForeignKey("business.id"))

    user = relationship("User", back_populates="reservations")
    business = relationship("Business", back_populates="reservations")
