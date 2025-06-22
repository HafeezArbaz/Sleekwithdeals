from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from typing import List
import os
import shutil
import uuid

from database import SessionLocal
from models import Store, ProductImage
from cors_config import add_cors
from database import engine
from models import Base

app = FastAPI()

# Enable CORS
add_cors(app)

Base.metadata.create_all(bind=engine)
# Create uploads folder if it doesn't exist
UPLOAD_DIR = "uploaded_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Serve images statically
app.mount("/uploaded_images", StaticFiles(directory=UPLOAD_DIR), name="uploaded_images")


@app.post("/products")
async def create_product(
    name: str = Form(...),
    price: float = Form(...),
    description: str = Form(...),
    images: List[UploadFile] = File(...)
):
    db = SessionLocal()

    # Create and save product
    product = Store(Name=name, Price=price, Description=description)
    db.add(product)
    db.commit()
    db.refresh(product)

    # Save uploaded images
    for image in images:
        file_ext = os.path.splitext(image.filename)[1]
        unique_filename = f"{uuid.uuid4()}{file_ext}"
        file_path = os.path.join(UPLOAD_DIR, unique_filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        image_url = f"/uploaded_images/{unique_filename}"
        db.add(ProductImage(product_id=product.ID, image_path=image_url))

    db.commit()
    db.close()

    return {"message": "Product created successfully"}


@app.get("/products")
def get_all_products():
    db = SessionLocal()
    products = db.query(Store).all()
    result = []

    for product in products:
        result.append({
            "id": product.ID,
            "name": product.Name,
            "price": product.Price,
            "description": product.Description,
            "images": [img.image_path for img in product.images]
        })

    db.close()
    return JSONResponse(content=result)
