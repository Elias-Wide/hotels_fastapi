from sqlalchemy import select
from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def get_by_id(cls, object_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=object_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()
