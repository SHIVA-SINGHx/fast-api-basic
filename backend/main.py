from fastapi import FastAPI
from pydantic import BaseModel
from models import Item
from database_models import Base


app = FastAPI()

database_model.Base.metadata.create_all(bind=engine)

class Item(BaseModel):
    name: str
    price: float
    is_available: bool = True 
    
    
Items = [
    Item(id=1, name="gaming laptop", description= "Asus tuff gaming laptop", price= 30000, quatity=12 ),
    Item(id=2, name="gaming pc", description= "gaming pc hai ye", price= 20000, quatity=1 ),
    Item(id=3, name="gaming phone", description= "iphone for gaming", price= 550000, quatity=3 ),
    Item(id=4, name="gaming laptop1", description= "acer gaming", price= 670000, quatity=14 ),
    Item(id=5, name="gaming laptop2", description= "lenovo gaming", price= 890000, quatity=21 )
]
    
@app.get("/")
def get_item(): 
    return{
        "message": "succesfully fatch",
        "data": Item
    }
    

    
@app.post("/item")
def create_item(item: Item):
    item_db.append(item)
    return {
        "message": "Item created successfully 🚀",
        "data": item
    }
    