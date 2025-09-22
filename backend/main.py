from fastapi import FastAPI, Depends, HTTPException
from database import create_db
import models, crud, schemas
from database import get_db, engine
from sqlalchemy.orm import Session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db()

@app.get("/products/", response_model= list[schemas.Product])
def get_all_products(db: Session= Depends(get_db)):
    return {crud.get_product,"Database connected successfully"}
