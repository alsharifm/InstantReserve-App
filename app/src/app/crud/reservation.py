from fastapi import status
from sqlalchemy.orm import Session

from sqlalchemy.exc import SQLAlchemyError
from app.models.reservation import Reservation
from app.schemas.reservation import ReservationCreate, ReservationUpdate




# Reservation CRUD Operations with enhanced error handling
def create_reservation(db: Session, reservation: ReservationCreate, user_id: int):
    db_reservation = Reservation(
        #**reservation.model_dump()
        creation_date = reservation.creation_date,
        party_size = reservation.party_size,
        reservation_time=reservation.reservation_time, 
        user_id= user_id, 
        )

    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    #{"success": True, "data": db_reservation, "error": None}
    return db_reservation

def get_reservation(db: Session, reservation_id: int):
    return db.query(Reservation).filter(Reservation.id == reservation_id).first()

def update_reservation(db: Session, reservation_id: int, reservation_data: ReservationUpdate):
    try:
        db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
        if db_reservation:  
            db_reservation.reservation_time = reservation_data.reservation_time

            db.commit()
            db.refresh(db_reservation)
        else:
            db_reservation = 0
        return db_reservation
    except SQLAlchemyError as e:
        db.rollback()
        return {"success": False, "error": {"code": 500, "message": "An unexpected error occurred."}}
    
def delete_reservation(db: Session, reservation_id: int):
    try:
        db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
        if db_reservation is None:
            return {"success": False, "error": {"code": 400, "message": "User not found"}}
        
        db.delete(db_reservation)
        db.commit()
        return {"success": True, "error": None}
    except SQLAlchemyError:
        db.rollback()
        return {"success": False, "error": {"code": 500, "message": "An unexpected error occurred."}}

def get_user_reservations(db: Session, user_id: int):
    return db.query(Reservation).filter(Reservation.user_id == user_id).all()