from fastapi import FastAPI
from database import create_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db()

@app.get("/")
def home():
    return {"msg": "Database connected successfully 🚀"}
