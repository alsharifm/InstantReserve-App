from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.crud.user as user_service
from app.core.auth import decode_access_token, oauth2_scheme
from app.dependencies import get_db

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.business import get_business
from app.schemas.business import Business

router = APIRouter()

@router.get("/businesses/{business_id}")
def read_business(business_id: int, db: Session = Depends(get_db)):
    db_business = get_business(db, business_id=business_id)
    if db_business is None:
        raise HTTPException(status_code=404, detail="Business not found")
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