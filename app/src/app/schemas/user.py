from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: str
    fullname: str
    phone: int


class UserCreate(UserBase):
    username: str
    email: str
    fullname: str
    phone: int
    password: str



class User(UserBase):
    id: int
    username: str
    email: str
    phone: int

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    phone: int

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    id: int
    username: str
    email: str
    phone: int


class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    phone: int

    class Config:
        from_attributes = True