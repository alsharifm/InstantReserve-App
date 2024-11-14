from pydantic import BaseModel
from datetime import datetime

class ReservationBase(BaseModel):
    location: str
    time: datetime
    party_size: int
    status: str

class ReservationCreate(ReservationBase):
    pass

class Reservation(ReservationBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True