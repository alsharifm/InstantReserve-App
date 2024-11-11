# routers/reservations.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import create_reservation
from schemas import ReservationCreate, Reservation
from database import get_db
from dependencies import get_current_user

router = APIRouter()

@router.post("/reservations/", response_model=Reservation)
def make_reservation(
    reservation: ReservationCreate, 
    db: Session = Depends(get_db), 
    current_user: int = Depends(get_current_user)
):
    return create_reservation(db=db, reservation=reservation, user_id=current_user.id)