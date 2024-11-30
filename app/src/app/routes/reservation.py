from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.auth import decode_access_token, oauth2_scheme
from app.dependencies import get_db
from app.crud.user import get_user_by_username
from sqlalchemy.orm import Session
from app.crud.reservation import create_reservation, get_reservation
from app.schemas.reservation import ReservationCreate, Reservation, ReservationUpdate, ReservationSchema

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

@router.delete("/api/reservation/{id}")
def delete_reservation(id: int, db: Session = Depends(get_db)):
    reservation = db.query(Reservation).filter(Reservation.id == id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    db.delete(reservation)
    db.commit()
    return {"success": True}

@router.put("/api/reservation/{id}", response_model=ReservationSchema)
def update_reservation(id: int, reservation_data: ReservationUpdate, db: Session = Depends(get_db)):
    reservation = db.query(Reservation).filter(Reservation.id == id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    for key, value in reservation_data.dict(exclude_unset=True).items():
        setattr(reservation, key, value)
    db.commit()
    db.refresh(reservation)
    return reservation