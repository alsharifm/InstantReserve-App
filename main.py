# main.py
from fastapi import FastAPI
from app.routers import users, reservations
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers for different API routes
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(reservations.router, prefix="/reservations", tags=["Reservations"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Instant Reserve API!"}