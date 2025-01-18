from sqlalchemy import select
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.rooms.models import Rooms


class RoomsDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def get_price_and_quantity(
        cls, room_id: int, session: async_session_maker
    ) -> tuple[int]:
        query = select(Rooms.price, Rooms.quantity).filter_by(id=room_id)
        result = await session.execute(query)
        return result.all()[0]
