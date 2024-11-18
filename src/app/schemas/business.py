from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class BusinessBase(BaseModel):
    business_name: str
    address: str
    business_email: str
    business_open: datetime
    business_phone: str
    category: str = "pending"

class Business(BusinessBase):
    id: int

    class Config:
        orm_mode = True