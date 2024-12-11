import secrets

from fastapi import HTTPException, status
from passlib.hash import bcrypt
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.security import verify_password
from app.models.business import Business
from app.schemas.business import BusinessCreate, BusinessUpdate

settings = get_settings()


# User CRUD operations
def get_business(db: Session, business_id: int):
    db_business = db.query(Business).filter(Business.id == business_id)
    if db_business :
        return db.query(Business).filter(Business.id == business_id).first()
    else:
        return {
        "success": False,
        "data": None,
        "error": {
            "code": status.HTTP_404_NOT_FOUND,
            "message": "User not found"
        }
    }

# Register a new user
def create_business(db: Session, business: BusinessCreate):

    db_business = Business(
        business_name = business.business_name,
        phone = business.phone,
        address = business.address,
        description = business.description,
    )

    db.add(db_business)
    db.commit()
    db.refresh(db_business)

    # TODO: Add functionality to send email verification code

    return db_business

def starter_businesses(db: Session, business: BusinessCreate):
    db_business = Business(
        business_name = "The Italian Bistro",
        phone = 123456789,
        address = "123 Main St, Springfield, IL",
        description = "Authentic Italian cuisine with a cozy atmosphere.",
    )
    create_business(db, db_business)
    
"""     db_business = Business(
        business_name = "The Italian Bistro",
        phone = 123456789,
        address = "123 Main St, Springfield, IL",
        description = "Authentic Italian cuisine with a cozy atmosphere.",
    )
    db_business = Business(
        business_name = "The Italian Bistro",
        phone = 123456789,
        address = "123 Main St, Springfield, IL",
        description = "Authentic Italian cuisine with a cozy atmosphere.",
    )
    db_business = Business(
        business_name = "The Italian Bistro",
        phone = 123456789,
        address = "123 Main St, Springfield, IL",
        description = "Authentic Italian cuisine with a cozy atmosphere.",
    ) """


