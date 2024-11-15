from pydantic import BaseModel
from datetime import datetime

class ReservationBase(BaseModel):
    location: str
    time: datetime
    party_size: int

class ReservationCreate(ReservationBase):
    pass

class Reservation(ReservationBase):
    id: int
    user_id: int
    business_id: int
    party_size: int
    reservationTime: int
    reservationDate: datetime

    class Config:
        orm_mode = True

class ReservationResponse(BaseModel):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ReservationUpdate(BaseModel):
    date_time: datetime = None
    user_id: int = None
    business_id: int = None