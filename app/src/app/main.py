from fastapi import FastAPI

from app.core.database import Bashatce, engine
from app.routes import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}