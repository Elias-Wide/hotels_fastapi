from fastapi import Depends, Request

from app.users.auth import get_user_id_from_token
from app.users.dao import UsersDAO
from app.users.exceptions import TokenException


async def get_token(request: Request):
    token = request.cookies.get("user_access_token")
    if not token:
        raise TokenException("error")
    return token


async def get_current_user(token: str = Depends(get_token)):
    user_id = await get_user_id_from_token(token)
    user = await UsersDAO.get_by_id(user_id)
    return user
