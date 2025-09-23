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

# get only one product
@app.get("/products/{id}", response_model=schemas.Product)
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product_queryset = crud.get_product_id(db, id)
    if product_queryset:
        return product_queryset
    raise HTTPException(status_code=404, detail="Invalid product id")

# create products
@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)
