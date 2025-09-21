from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_available: bool = True   # default value
    
    
    
item_db = []
    

@app.post("/item")
def create_item(item: Item):
    item_db.append(item)
    return {
        "message": "Item created successfully 🚀",
        "data": item
    }
    
@app.get("/")
def get_item():
    return{
        "message": "succesfully fatch",
        "data": item_db
    }