from fastapi import FastAPI
from app.routes import api_router
from app.core.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI()

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


    