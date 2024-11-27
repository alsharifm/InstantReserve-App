from fastapi import FastAPI
from src.app.core.database import engine, Base
from src.app.routes import user, reservations, business


# Initialize the FastAPI app
app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include the routers
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(reservations.router, prefix="/reservations", tags=["Reservations"])
app.include_router(business.router, prefix="/business", tags=["Business"])

#Optional: Add CORS or other middleware if needed

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
     CORSMiddleware,
     allow_origins=["*"],
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcomeeeeeeeeeeeeeeee///// to the Instant Reserve API"}

    ##PYTHONPATH=src uvicorn app.main:app --reload

    