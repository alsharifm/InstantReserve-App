from fastapi import APIRouter

from app.routes import business, reservations, user

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["Users"])
api_router.include_router(reservations.router, prefix="/categories", tags=["Categories"])
api_router.include_router(
    business.router, prefix="/transactions", tags=["Transactions"]
)
