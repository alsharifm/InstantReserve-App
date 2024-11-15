from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class BusinessBase(BaseModel):
    business_name: str
    address: str
    business_email: str
    business_open: datetime
    business_phone: str
    category: str = "pending"

class BusinessCreate(BusinessBase):
    pass

class Business(BusinessBase):
    id: int

    class Config:
       from_attributes = True
