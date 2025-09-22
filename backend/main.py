from fastapi import FastAPI, Depends, HTTPException
from database import create_db
import models, crud, schemas
from database import get_db, engine
from sqlalchemy.orm import Session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db()

# get products
@app.get("/products/", response_model= list[schemas.Product])
def get_all_products(db: Session= Depends(get_db)):
    return crud.get_product(db)

# create products
@app.post("/prodcuts/", response_model = list[schemas.Product])
def create_prodcuts(product: schemas.ProductCreate, db: Session= Depends(get_db)):
    return crud.create_product(db,product)