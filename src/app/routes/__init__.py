from fastapi import APIRouter

from src.app.routes import business, reservations, user

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["Users"])
api_router.include_router(reservations.router, prefix="/reservations", tags=["Reservations"])
api_router.include_router(business.router, prefix="/business", tags=["Business"]
)
