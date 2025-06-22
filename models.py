# models.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Store(Base):
    __tablename__ = "Store"

    ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Price = Column(Float)
    Description = Column(String)

    images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")


class ProductImage(Base):
    __tablename__ = "ProductImage"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("Store.ID"))
    image_path = Column(String)

    product = relationship("Store", back_populates="images")
