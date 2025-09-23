from pydantic import BaseModel



class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    
class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    
    class config:
        # orm_mode = True
        from_attribute = True
    