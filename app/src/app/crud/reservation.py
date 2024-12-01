from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.auth import decode_access_token, oauth2_scheme
from app.dependencies import get_db
from app.crud.user import get_user_by_username
from sqlalchemy.exc import SQLAlchemyError
from app.schemas.reservation import ReservationCreate, Reservation, ReservationUpdate
from app.schemas.user import UserUpdate


# Reservation CRUD Operations with enhanced error handling
def create_reservation(db: Session, reservation: ReservationCreate, user_id: int):
    db_reservation = Reservation(
        location=reservation.location,
        time=reservation.time,
        user_id=user_id,
        business_id=reservation.business_id,  # Dynamic business_id
        party_size=reservation.party_size,
        reservationTime=reservation.reservationTime,
        reservationDate=reservation.reservationDate,
        date_time=reservation.date_time,
    )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return {"success": True, "data": db_reservation, "error": None}  # Return the reservation object

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