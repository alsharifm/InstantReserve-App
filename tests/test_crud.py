# app/tests/test_user_crud.py

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from src.app.models.user import User
from src.app.schemas.user import UserCreate, UserUpdate
from src.app.crud.user import (
    create_user,
    get_user,
    update_user,
    delete_user,
    get_user_by_username,
)
from src.app.core.database import Base

# Setup test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def test_db():
    # Create the tables in the test database
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db  # Provide the fixture value
    db.close()
    # Drop the tables after the test session
    Base.metadata.drop_all(bind=engine)

def test_create_user(test_db):
    user_data = UserCreate(username="johndoe", email="johndoe@example.com", password="securepassword", phone="1234567890", fullname="John Doe")
    user = create_user(test_db, user_data)
    assert user.username == "johndoe"
    assert user.email == "johndoe@example.com"

    # Testing duplicate user creation, should raise an HTTPException
    with pytest.raises(IntegrityError):
        create_user(test_db, user_data)

def test_get_user(test_db):
    user = get_user(test_db, user_id=1)
    assert user is not None
    assert user.username == "johndoe"
    assert user.email == "johndoe@example.com"

    # Test getting a non-existent user
    non_existent_user = get_user(test_db, user_id=999)
    assert non_existent_user == {
        "success": False,
        "data": None,
        "error": {
            "code": 404,
            "message": "User not found"
        }
    }

def test_update_user(test_db):
    update_data = UserUpdate(username="johnsmith", email="johnsmith@example.com", phone="0987654321")
    updated_user_response = update_user(test_db, user_id=1, user_data=update_data)
    
    assert updated_user_response["success"] is True
    assert updated_user_response["user"]["name"] == "johnsmith"
    assert updated_user_response["user"]["email"] == "johnsmith@example.com"

    # Test updating a non-existent user
    non_existent_update_response = update_user(test_db, user_id=999, user_data=update_data)
    assert non_existent_update_response == {
        "success": False,
        "error": {"code": 400, "message": "User not found"}
    }

def test_delete_user(test_db):
    delete_response = delete_user(test_db, user_id=1)
    assert delete_response["success"] is True
    assert delete_response["error"] is None

    # Test deleting a non-existent user
    non_existent_delete_response = delete_user(test_db, user_id=999)
    assert non_existent_delete_response == {
        "success": False,
        "error": {"code": 400, "message": "User not found"}
    }