from fastapi import FastAPI, Query
from datetime import date
from typing import Optional

from pydantic import BaseModel
from app.bookings.router import router as router_bookings
from app.users.router import router as router_users

app = FastAPI()
app.include_router(router_users)
app.include_router(router_bookings)


class SHotel(BaseModel):
    addres: str
    name: str
    stars: int


@app.get("/hotels")
def get_hotels(
    location: str,
    bed_number: int,
    date_from: date,
    date_to: date,
    stars: Optional[int] = Query(None, ge=1, le=5),
    has_spa: Optional[bool] = None,
) -> list[SHotel]:
    return date_to, date_from
