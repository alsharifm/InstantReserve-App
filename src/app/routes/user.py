from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.app.core.auth import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
    decode_access_token,
    oauth2_scheme,
)
from src.app.dependencies import get_db
from src.app.schemas.token import Token
from src.app.schemas.user import UserCreate, UserResponse, UserUpdate, User, UserSchema
from src.app.crud.user import delete_user, update_user, get_user, create_user, get_user_by_email
from typing import List

router = APIRouter()

@router.post("/users/", response_model=User)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)  # Assuming email should be checked elsewhere
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/api/users/{id}")
def delete_user_endpoint(id: int, db: Session = Depends(get_db)):
    result = delete_user(db, id)
    if not result["success"]:
        raise HTTPException(status_code=result["error"]["code"], detail=result["error"]["message"])
    return {"success": True}


@router.put("/api/users/{id}", response_model=UserResponse)
def update_user_endpoint(id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    result = update_user(db, id, user_data)
    if not result["success"]:
        raise HTTPException(status_code=result["error"]["code"], detail=result["error"]["message"])
    return result


@router.get("/api/users", response_model=List[UserSchema])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users