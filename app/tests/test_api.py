# app/tests/test_api_endpoints.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.app.main import app
from src.app.core.database import Base
from src.app.dependencies import get_db
from src.app.schemas.user import UserCreate, UserUpdate
from src.app.schemas.reservation import ReservationCreate, ReservationUpdate
from datetime import datetime

# Setup the test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency to use the test database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Initialize the test client
client = TestClient(app)

# Setup and teardown of the database
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)  # Create tables
    yield
    Base.metadata.drop_all(bind=engine)  # Drop tables after tests

def test_create_user():
    user_data = {"username": "testuser", "email": "testuser@example.com", "password": "password123", "phone": "1234567890", "fullname": "Test User"}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "testuser@example.com"

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_update_user():
    update_data = {"username": "updateduser", "email": "updateduser@example.com"}
    response = client.put("/api/users/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["user"]["name"] == "updateduser"
    assert response.json()["user"]["email"] == "updateduser@example.com"

def test_delete_user():
    response = client.delete("/api/users/1")
    assert response.status_code == 200
    assert response.json()["success"] is True

    # Verify user deletion
    response = client.get("/users/1")
    assert response.status_code == 404

def test_get_users():
    response = client.get("/api/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_reservation():
    reservation_data = {
        "user_id": 1,
        "business_id": 1,
        "date_time": datetime.utcnow().isoformat(),
        "party_size": 2,
    }
    response = client.post("/reservations/", json=reservation_data)
    assert response.status_code == 200
    assert response.json()["user_id"] == 1
    assert response.json()["party_size"] == 2

def test_get_reservation():
    response = client.get("/reservations/1")
    assert response.status_code == 200
    assert response.json()["user_id"] == 1

def test_update_reservation():
    update_data = {"party_size": 4}
    response = client.put("/api/reservation/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["party_size"] == 4

def test_delete_reservation():
    response = client.delete("/api/reservation/1")
    assert response.status_code == 200
    assert response.json()["success"] is True

    # Verify reservation deletion
    response = client.get("/reservations/1")
    assert response.status_code == 404

def test_get_business():
    response = client.get("/businesses/1")
    assert response.status_code == 404  # Expecting not found since we haven't created any businesses yet

# Add additional tests for creating a business if needed.