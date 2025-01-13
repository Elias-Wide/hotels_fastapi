from app.bookings.models import Bookings
from app.dao.base import BaseDAO


class BookingsDAO(BaseDAO):
    model = Bookings
