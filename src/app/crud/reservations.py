from sqlalchemy.orm import Session
from src.app.models.reservations import Reservation
from src.app.schemas.reservations import ReservationCreate, ReservationUpdate
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError


# Reservation CRUD Operations with enhanced error handling
def create_reservation(db: Session, reservation: ReservationCreate, user_id: int):
    db_reservation = Reservation(date_time=reservation.date_time, user_id=user_id, business_id=reservation.business_id)
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return {"success": True, "data": db_reservation, "error": None}

def get_reservation(db: Session, reservation_id: int):
    db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if db_reservation:
        return {"success": True, "data": db_reservation, "error": None}
    return {
        "success": False,
        "data": None,
        "error": {
            "code": status.HTTP_404_NOT_FOUND,
            "message": "Reservation not found"
        }
    }

def update_reservation(db: Session, reservation_id: int, reservation_data: ReservationUpdate):
    try:
        db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
        if db_reservation is None:
            return {"success": False, "error": {"code": 400, "message": "Reservation not found"}}
        
        for key, value in reservation_data.dict(exclude_unset=True).items():
            setattr(db_reservation, key, value)
        
        db.commit()
        db.refresh(db_reservation)
        return {
            "success": True,
            "reservation": {
                "date": db_reservation.date,
                "time": db_reservation.time,
                "party_size": db_reservation.party_size,
                "status": db_reservation.status,
            },
            "error": None
        }
    except SQLAlchemyError as e:
        db.rollback()
        return {"success": False, "error": {"code": 500, "message": "An unexpected error occurred."}}