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

def get_product_id(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def update_product(db: Session, product: ProductCreate, item_id: int):
    product_queryset = db.query(Item).filter(Item.id == item_id).first()
    if product_queryset:
        for key, value in product.dict().items():  
            setattr(product_queryset, key, value)

        db.commit()
        db.refresh(product_queryset)
        return product_queryset
    
def delete_product(db: Session, id: int):
    product_queryset = db.query(Item).filter(Item.id == id).first()
    if product_queryset:
        db.delete(product_queryset)
        db.commit()
        
        return product_queryset