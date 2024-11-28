from pydantic import BaseModel
from datetime import datetime

class ReservationBase(BaseModel):
    location: str
    time: datetime
    party_size: int

class ReservationCreate(ReservationBase):
    id: int
    user_id: int
    business_id: int
    party_size: int
    reservationTime: int
    reservationDate: datetime
    date_time: datetime

    class Config:
        from_attributes = True

class Reservation(ReservationBase):
    id: int
    user_id: int
    business_id: int
    party_size: int
    reservationTime: int
    reservationDate: datetime

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
    business_id: int = None

class ReservationSchema(BaseModel):
    id: int
    user_id: int
    business_id: int
    date_time: datetime

    class Config:
        from_attributes = True