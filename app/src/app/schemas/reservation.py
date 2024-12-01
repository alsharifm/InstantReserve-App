from pydantic import BaseModel, ValidationError
from datetime import datetime
from typing import Optional

class ReservationBase(BaseModel):
    user_id: int
    party_size: int
    reservationTime: int
    reservationDate: datetime
    date_time: datetime

class ReservationCreate(ReservationBase):
    user_id: int
    party_size: int
    reservationTime: int
    reservationDate: datetime
    date_time: datetime  # Inherit all fields from ReservationBase without redefining

class Reservation(ReservationBase):
    id: int

    class Config:
        from_attributes = True

class ReservationResponse(BaseModel):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ReservationUpdate(BaseModel):
    date_time: datetime = None
    user_id: int = None

class ReservationSchema(BaseModel):
    id: int
    user_id: int
    date_time: datetime

    class Config:
        from_attributes = True