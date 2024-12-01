from pydantic import BaseModel, ValidationError
from datetime import datetime
from typing import Optional

class ReservationBase(BaseModel):
    location: str
    time: int
    user_id: int
    business_id: int
    party_size: int
    reservationTime: int
    reservationDate: datetime
    date_time: datetime

class ReservationCreate(ReservationBase):
    pass  # Inherit all fields from ReservationBase without redefining

class Reservation(ReservationBase):
    id: Optional[int]  # Add the `id` field to represent the complete reservation object
try:
     Reservation()
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'missing'

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