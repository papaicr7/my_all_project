from sqlalchemy import Column, BigInteger, String, Integer, Enum, DateTime, func
from database import Base

class CategoryEnum(str, Enum):
    FINISHED = "finished"
    SEMI_FINISHED = "semi-finished"
    RAW = "raw"

class UOMEnum(str, Enum):
    METER = "mtr"
    MILLIMETER = "mm"
    LITER = "ltr"
    MILLILITER = "ml"
    CENTIMETER = "cm"
    MILLIGRAM = "mg"
    GRAM = "gm"
    UNIT = "unit"
    PACK = "pack"

class Product(Base):
    __tablename__ = "products"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    category = Column(Enum(CategoryEnum), nullable=False)
    description = Column(String(250))
    product_image = Column(String(500))
    sku = Column(String(100), unique=True)
    unit_of_measure = Column(Enum(UOMEnum), nullable=False)
    lead_time = Column(Integer)
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, default=func.now(), onupdate=func.now())

