from fastapi import APIRouter

from app.routes import reservation, user, business

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["Users"])
api_router.include_router(reservation.router, prefix="/reservations", tags=["Reservations"])
api_router.include_router(business.router, prefix="/businesses", tags=["Businesses"])