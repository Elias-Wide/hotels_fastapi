from datetime import date
from typing import List

from pydantic import BaseModel
from sqlalchemy import JSON


class SBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int

    class Config:
        from_attributes = True


class SBookingGet(BaseModel):
    id: int
    date_from: date
    date_to: date
    price_per_day: int
    total_days: int
    total_cost: int
    user_id: int
    room_id: int
    name: str
    description: str
    services: List[str]
    image_id: str

    class Config:
        from_attributes = True
