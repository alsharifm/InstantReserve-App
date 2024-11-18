from sqlalchemy.orm import Session
from src.app.models.business import Business
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status


# Business CRUD Operations with enhanced error handling
def get_business(db: Session, business_id: int):
    db_business = db.query(Business).filter(Business.id == business_id).first()
    if db_business:
        return {
            "success": True,
            "data": {
                "id": db_business.id,
                "business_name": db_business.business_name,
                "address": db_business.address,
                "business_email": db_business.business_email,
                "business_open": db_business.business_open,
                "business_phone": db_business.business_phone,
                "category": db_business.category
            },
            "error": None
        }
    return {
        "success": False,
        "data": None,
        "error": {
            "code": status.HTTP_404_NOT_FOUND,
            "message": "Business not found"
        }
    }