from fastapi import FastAPI, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Product
from schemas import ProductCreate, ProductResponse, ProductUpdate
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/product/list", response_model=list[ProductResponse])
def list_products(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    offset = (page - 1) * page_size
    return db.query(Product).offset(offset).limit(page_size).all()

@app.get("/product/{pid}/info", response_model=ProductResponse)
def product_info(pid: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == pid).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/product/add", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.put("/product/{pid}/update", response_model=ProductResponse)
def update_product(pid: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == pid).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for key, value in product.model_dump(exclude_unset=True).items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product