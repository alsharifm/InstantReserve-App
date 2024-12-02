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