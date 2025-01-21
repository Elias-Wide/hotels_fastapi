from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy import select

from app.bookings.dao import BookingsDAO
from app.bookings.exceptions import RoomCantBeBooked
from app.bookings.schemas import SBooking, SBookingGet
from app.users.dependencies import get_current_user
from app.users.exceptions import AccessDeniedException
from app.users.models import Users
from app.users.permissions import is_admin

router = APIRouter(prefix="/bookings", tags=["Бронирование"])


@router.get("")
async def get_bookings(
    user: Users = Depends(get_current_user),
) -> list[SBookingGet]:
    return await BookingsDAO.get_bookings_by_user(user.id)


@router.get("/all")
async def get_bookings(
    user: Users = Depends(get_current_user),
) -> list[SBookingGet]:
    if not is_admin(user):
        raise AccessDeniedException()
    return await BookingsDAO.find_all()

@router.post("")
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user),
) -> SBooking:
    booking = await BookingsDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCantBeBooked()
    return booking
