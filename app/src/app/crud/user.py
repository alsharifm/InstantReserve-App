import secrets

from fastapi import HTTPException
from passlib.hash import bcrypt
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.security import verify_password
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from sqlalchemy.orm import Session
from app.models.reservation import Reservation
from app.models.business import Business
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError



settings = get_settings()


# User CRUD operations
def get_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id)
    if db_user :
        return db.query(User).filter(User.id == user_id).first()
    else:
        return {
        "success": False,
        "data": None,
        "error": {
            "code": status.HTTP_404_NOT_FOUND,
            "message": "User not found"
        }
    }

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


# Register a new user
def create_user(db: Session, user: UserCreate):
    if get_user_by_username(db, user.username) or get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=400, detail="Username or email already registered"
        )

    password_hash = bcrypt.hash(user.password)
    verification_code = secrets.token_urlsafe(32)

    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=password_hash,
        verification_code=verification_code,
        phone = user.phone,
        fullname = user.fullname,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # TODO: Add functionality to send email verification code

    return db_user


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)

    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user


def verify_email(verification_code: str, db: Session):
    # TODO: Implement email verification
    pass



def delete_user(db: Session, user_id: int):
    try:
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            return {"success": False, "error": {"code": 400, "message": "User not found"}}
        
        db.delete(db_user)
        db.commit()
        return {"success": True, "error": None}
    except SQLAlchemyError:
        db.rollback()
        return {"success": False, "error": {"code": 500, "message": "An unexpected error occurred."}}
    

def update_user(db: Session, user_id: int, user: UserUpdate):
    try:
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:  
            db_user.username = user.username
            db_user.email = user.email
            db_user.phone = user.phone
        
            db.commit()
            db.refresh(db_user)
        else:
            db_user = 0
        return db_user
    except SQLAlchemyError:
        db.rollback()
        return {"success": False, "error": {"code": 500, "message": "An unexpected error occurred."}}
    
##Users may not need to access all users, will get back to it if needed
#def get_all_users(db: Session, user_id: int):
#    db_user = db.query(User).filter(User.id == user_id)
#    if db_user :
#        return db.query(User).filter(User.id == user_id).first()
#    else:
#        return {
#        "success": False,
#        "data": None,
#        "error": {
#            "code": status.HTTP_404_NOT_FOUND,
#            "message": "User not found"
#        }
#    }