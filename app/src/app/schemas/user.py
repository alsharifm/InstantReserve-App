from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: str
    fullname: str
    phone: str


class UserCreate(UserBase):
    username: str
    email: str
    fullname: str
    phone: str
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    phone: str

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    id: int
    username: str
    email: EmailStr
    phone: str


class UserSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str

    class Config:
        from_attributes = True