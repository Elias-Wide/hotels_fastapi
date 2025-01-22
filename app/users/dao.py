from sqlalchemy import insert
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.users.constants import ADMIN
from app.users.models import Users


class UsersDAO(BaseDAO):
    model = Users

    @classmethod
    async def create_user_admin(cls, email: str, hashed_password: str):
        """Создание профиля админа."""
        async with async_session_maker() as session:
            query = (
                insert(cls.model)
                .values(
                    email=email, hashed_password=hashed_password, role=ADMIN
                )
                .returning(cls.model)
            )
            object = await session.execute(query)
            await session.commit()
            return object.scalar_one_or_none()
