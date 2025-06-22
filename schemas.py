from typing import List
from pydantic import BaseModel

class StoreCreate(BaseModel):
    ID: str
    Name: str
    Price: int
    Image: str
    Description: str

class StoreResponse(BaseModel):
    id: int
    Name: str
    Price: float
    Description: str
    images: List[str]