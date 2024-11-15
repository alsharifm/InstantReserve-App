from pydantic import BaseModel
from datetime import datetime


class ReservationBase(BaseModel):
    date_time: datetime
    user_id: int
    business_id: int

class ReservationCreate(ReservationBase):
    pass

class Reservation(ReservationBase):
    id: int

    class Config:
        from_attributes = True

class ReservationUpdate(BaseModel):
    date_time: datetime = None
    user_id: int = None
    business_id: int = None
