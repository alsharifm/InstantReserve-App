from fastapi import FastAPI
from app.routes import api_router
from src.app.core.database import engine, Base
from src.app.routes import user, reservation, business
from fastapi.middleware.cors import CORSMiddleware


# Initialize the FastAPI app
app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include the routers
#app.include_router(user.router, prefix="/users", tags=["Users"])
#app.include_router(reservation.router, prefix="/reservations", tags=["Reservations"])
#app.include_router(business.router, prefix="/business", tags=["Business"])
app.include_router(api_router)

app.add_middleware(
     CORSMiddleware,
     allow_origins=["*"],
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Instant Reserve API"}


    