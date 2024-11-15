from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: str
    fullname: str
    phone: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_date: datetime

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    username: str
    email: str
    phone: str