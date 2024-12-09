from pydantic import BaseModel
from datetime import datetime


class ReservationCreate(BaseModel):
    party_size: int
    reservation_time: int
    business_name: str
    creation_date: datetime


class Reservation(BaseModel):
    id: int
    party_size: int
    reservation_time: int
    business_name: str
    creation_date: datetime

    class Config:
        from_attributes = True

class ReservationResponse(BaseModel):
    id: int


    class Config:
        from_attributes = True

class ReservationUpdate(BaseModel):
    party_size: int

class ReservationSchema(BaseModel):
    id: int
    reservation_time: int

    class Config:
        from_attributes = True