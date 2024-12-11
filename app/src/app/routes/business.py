from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import app.crud.business as business_service
from app.dependencies import get_db
from app.schemas.business import BusinessCreate, Business
from app.crud.business import get_business, create_business

router = APIRouter()

@router.post("/business/", response_model=Business)
def register_business(business: BusinessCreate, db: Session = Depends(get_db)):
    return create_business(db=db, business=business)


@router.get("/business/{business_id}", response_model=Business)
def read_business(business_id: int, db: Session = Depends(get_db)):
    db_business = get_business(db, business_id=business_id)
    if db_business is None:
        raise HTTPException(status_code=404, detail="business not found")
    return db_business


