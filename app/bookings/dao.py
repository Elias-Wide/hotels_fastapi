from datetime import date

from sqlalchemy import and_, func, insert, or_, select, text
from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker, engine
from app.rooms.dao import RoomsDAO
from app.rooms.models import Rooms


class BookingsDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(cls, user_id: int, room_id: int, date_from: date, date_to: date):
        async with async_session_maker() as session:
            booked_rooms = select(Bookings).where(
                and_(
                    Bookings.room_id == room_id,
                    or_(
                        and_(
                            Bookings.date_from >= date_from,
                            Bookings.date_from <= date_to,
                        ),
                        and_(
                            Bookings.date_from <= date_from,
                            Bookings.date_to > date_to,
                        ),
                    ),
                )
            )
            booked_rooms = await session.execute(
                select(func.count("*")).select_from(booked_rooms)
            )

            price, room_quantity = await RoomsDAO.get_price_and_quantity(
                room_id, session
            )
            if room_quantity - booked_rooms.scalar() > 0:
                add_booking = (
                    insert(Bookings)
                    .values(
                        room_id=room_id,
                        user_id=user_id,
                        date_from=date_from,
                        date_to=date_to,
                        price=price,
                    )
                    .returning(Bookings)
                )
                new_booking = await session.execute(add_booking)
                await session.commit()
                return new_booking.scalar()
            else:
                return None

    @classmethod
    async def get_bookings_by_user(cls, user_id) -> list[Bookings]:
        async with async_session_maker() as session:
            bookings = await session.execute(
                select(Bookings)
                .order_by(Bookings.date_from)
                .where(Bookings.user_id == user_id)
            )
        return bookings.scalars().all()
