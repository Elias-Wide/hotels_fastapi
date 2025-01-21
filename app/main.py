from fastapi import FastAPI

from app.bookings.router import router as router_bookings
from app.frontend.pages.router import router as router_pages
from app.hotels.router import router as router_hotels
from app.users.router import router as router_users

app = FastAPI()
app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_pages)


# @app.get("/hotels")
# def get_hotels(
#     location: str,
#     bed_number: int,
#     date_from: date,
#     date_to: date,
#     stars: Optional[int] = Query(None, ge=1, le=5),
#     has_spa: Optional[bool] = None,
# ) -> list[SHotel]:
#     return date_to, date_from
