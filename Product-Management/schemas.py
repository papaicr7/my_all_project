from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class CategoryEnum(str, Enum):
    finished = "finished"
    semi_finished = "semi-finished"
    raw = "raw"

class UOMEnum(str, Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    ml = "ml"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    pack = "pack"

class ProductBase(BaseModel):
    name: str
    category: CategoryEnum
    description: str | None = None
    product_image: str | None = None
    sku: str
    unit_of_measure: UOMEnum
    lead_time: int | None = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        from_attributes = True