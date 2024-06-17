from fastapi import FastAPI
from app.routes import data

app = FastAPI()

app.include_router(data.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Gokada Logistics Optimization API"}
