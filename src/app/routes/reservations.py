from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import app.crud.reservations as category_service
from src.app.core.auth import decode_access_token, oauth2_scheme
from src.app.dependencies import get_db
from src.app.crud.user import get_user_by_username
from sqlalchemy.orm import Session
from src.app.crud.reservations import create_reservation, get_reservation
from src.app.schemas.reservations import ReservationCreate, Reservation

router = APIRouter()

@router.post("/reservations/", response_model=Reservation)
def add_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    return create_reservation(db=db, reservation=reservation, user_id=reservation.user_id)

@router.get("/reservations/{reservation_id}", response_model=Reservation)
def read_reservation(reservation_id: int, db: Session = Depends(get_db)):
    db_reservation = get_reservation(db, reservation_id=reservation_id)
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return db_reservation