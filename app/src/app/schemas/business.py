from pydantic import BaseModel


class BusinessBase(BaseModel):
    business_name: str
    phone: int
    address: str
    description: str

class BusinessCreate(BusinessBase):
    business_name: str
    phone: int
    address: str
    description: str


class Business(BusinessBase):
    business_name: str
    phone: int
    address: str
    description: str

    class Config:
        from_attributes = True


class BusinessResponse(BaseModel):
    business_name: str
    phone: int
    address: str
    description: str

    class Config:
        from_attributes = True

class BusinessUpdate(BaseModel):
    business_name: str
    phone: int
    address: str
    description: str


class BusinessSchema(BaseModel):
    business_name: str
    phone: int
    address: str
    description: str

    class Config:
        from_attributes = True