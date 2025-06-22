from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Store(Base):
    __tablename__ = "Store"
    ID = Column(Integer, primary_key=True, index=True, autoincrement=True)  # ✅
    Name = Column(String)
    Price = Column(Float)
    Description = Column(String)
    images = relationship("ProductImage", back_populates="product")

class ProductImage(Base):
    __tablename__ = "ProductImage"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # ✅
    product_id = Column(Integer, ForeignKey("Store.ID"))
    image_path = Column(String)
    product = relationship("Store", back_populates="images")
