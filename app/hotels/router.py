from datetime import date, datetime
from fastapi import APIRouter, Query


from app.bookings.validators import validate_date
from app.hotels.dao import HotelsDAO
from app.hotels.exceptions import InValidDate
from app.hotels.schemas import SHotelInfo


router = APIRouter(prefix="/hotels", tags=["Отели"])


@router.get("")
async def get_hotels_by_location_and_date(
    location: str,
    date_from: date = Query(
        ..., description=f"Например {datetime.now().date()}"
    ),
    date_to: date = Query(
        ..., description=f"Например {datetime.now().date()}"
    ),
) -> list[SHotelInfo]:
    await validate_date(date_from, date_to)
    hotels = await HotelsDAO.seacrh_for_hotels(location, date_from, date_to)
    return hotels
