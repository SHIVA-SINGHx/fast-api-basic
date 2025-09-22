from fastapi import FastAPI

from pydantic import BaseModel
from models import Item
from database_models import Base



app = FastAPI()


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
    
    
todos = []

@app.get("/")
def get_product():
    return todos