from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_available: bool = True 
    
    
    
item_db = []
    

@app.get("/items")
def get_item():
    session
    return{
        "message": "succesfully fatch",
        "data": item_db
    }
    
@app.post("/item")
def create_item(item: Item):
    item_db.append(item)
    return {
        "message": "Item created successfully 🚀",
        "data": item
    }
    