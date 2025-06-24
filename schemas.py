from typing import List
from pydantic import BaseModel

class StoreCreate(BaseModel):
    Name: str
    Price: float
    Description: str
    Category: str
    SubCategory: Optional[str] = None

class StoreResponse(BaseModel):
    id: int
    Name: str
    Price: float
    Description: str
    images: List[str]