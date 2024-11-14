from pydantic import BaseModel
from datetime import datetime

class BusinessBase(BaseModel):
    name: str
    email: str
    location: str

class Business(UserBase):
    id: int

    class Config:
        orm_mode = True