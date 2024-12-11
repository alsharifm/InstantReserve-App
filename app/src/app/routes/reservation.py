from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.auth import decode_access_token, oauth2_scheme
from app.dependencies import get_db
from app.crud.user import get_user_by_username
from app.crud.reservation import create_reservation, get_reservation, update_reservation, delete_reservation
from app.crud.reservation import get_user_reservations as fetch_user_reservations
from app.schemas.reservation import ReservationCreate, Reservation, ReservationUpdate, ReservationSchema
import app.crud.user as user_service

router = APIRouter()

@router.post("/reservations/", response_model=Reservation)
def add_reservation(reservation: ReservationCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme),):
        username = decode_access_token(token).username
        user_id = user_service.get_user_by_username(db, username).id
        return create_reservation(db, reservation, user_id)

@router.get("/reservations/user", response_model=list[Reservation], tags=["Reservations"])
async def get_user_reservations(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    """
    Endpoint to fetch all reservations for the authenticated user.

    Args:
        token (str): The access token for the user.
        db (Session): The database session.

    Returns:
        list[ReservationSchema]: A list of reservations for the user.
    """
    decoded_token = decode_access_token(token)
    if decoded_token is None or decoded_token.username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
    username = decoded_token.username
    user = get_user_by_username(db, username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    # Fetch reservations using the new CRUD function
    user_reservations = fetch_user_reservations(db, user.id)

    return user_reservations

@router.get("/reservations/{reservation_id}", response_model=Reservation)
def read_reservation(reservation_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_reservation = get_reservation(db, reservation_id=reservation_id)
    username = decode_access_token(token).username
    user_id = user_service.get_user_by_username(db, username).id
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return db_reservation


@router.delete("/api/reservation/{id}")
def cancel_reservation(id: int, db: Session = Depends(get_db, )):
    result = delete_reservation(db, id)
    if not result["success"]:
        raise HTTPException(status_code=result["error"]["code"], detail=result["error"]["message"])
    return {"success": True}

@router.put("/api/reservation/{id}", response_model=ReservationSchema)
def update_reservation_endpoint(id: int, reservation_data: ReservationUpdate, db: Session = Depends(get_db)):
    updated_reservation = update_reservation(db, id, reservation_data)
    if updated_reservation == 0:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return updated_reservation