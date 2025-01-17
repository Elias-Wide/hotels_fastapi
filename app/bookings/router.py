from datetime import date
from fastapi import APIRouter, Depends, Request
from sqlalchemy import select

from app.bookings.dao import BookingsDAO
from app.bookings.models import Bookings
from app.bookings.schemas import SBooking
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(prefix="/bookings", tags=["Бронирование"])


@router.get("")
async def get_bookings(
    user: Users = Depends(get_current_user),
) -> list[SBooking]:
    return await BookingsDAO.find_all(user_id=user.id)


@router.post("")
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user),
):
    print(user.id, type(user.id), '!!!!!!!!!!!!!!!!11')
    await BookingsDAO.add(
        user.id,
        room_id,
        date_from,
        date_to,
    )
