from models import Item
from sqlalchemy.orm import Session
from schemas import ProductCreate



def create_product(db: Session, data: ProductCreate):
    product_instance = Item(**data.model_dump())
    db.add(product_instance)
    db.commit()
    db.refresh(product_instance)
    return product_instance
    
def get_product(db: Session):
    return db.query(Item).all()