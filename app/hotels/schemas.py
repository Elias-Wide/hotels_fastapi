from typing import List
from pydantic import BaseModel


class SHotelInfo(BaseModel):
    id: int
    name: str
    location: str
    services: List[str]
    rooms_quantity: int
    image_id: int
    available_rooms: int

    class Config:
        from_attributes = True
