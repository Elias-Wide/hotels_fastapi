from fastapi import APIRouter
from sqlalchemy import select

from app.bookings.dao import BookingsDAO
from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker


router = APIRouter(prefix="/bookings", tags=["Бронирование"])


@router.get("")
async def get_bookings():
    return await BookingsDAO.get_by_id(2)
