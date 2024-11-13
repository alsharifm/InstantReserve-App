# crud.py
from sqlalchemy.orm import Session
from models import User, Reservation
from schemas import UserCreate, ReservationCreate
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#def get_user_by_email(db: Session, email: str):
#    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    try:
        # Hash the user's password
        hashed_password = pwd_context.hash(user.password)
        
        # Create a new user instance
        db_user = User(username=user.name, email=user.email, password=hashed_password, phone=user.phone)
        
        # Add and commit the new user to the database
        db.add(db_user)
        db.commit()
        
        # Refresh the instance to get the new user’s details (e.g., ID)
        db.refresh(db_user)
        
        # Return a successful response with the user data
        return {
            "success": True,
            "user": {
                "name": db_user.username,
                "email": db_user.email,
                "phone": db_user.phone
            },
            "error": None
        }
    except IntegrityError:
        # Rollback the transaction to prevent partial saves
        db.rollback()
        
        # Return an error response if the email is already in use or other integrity issue
        return {
            "success": False,
            "user": None,
            "error": {
                "code": status.HTTP_400_BAD_REQUEST,
                "message": "User with this email already exists"
            }
        }
    except Exception as e:
        # Handle any other unexpected errors
        db.rollback()
        
        return {
            "success": False,
            "user": None,
            "error": {
                "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "An unexpected error occurred. Please try again later."
            }
        }

def create_reservation(db: Session, reservation: ReservationCreate, user_id: int):
    db_reservation = Reservation(date=reservation.date)
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def get_user(db: Session, user)
