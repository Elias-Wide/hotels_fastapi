from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException, status
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.config import settings
from app.users.dao import UsersDAO
from app.users.exceptions import TokenException
from app.users.models import Users

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def authenticate_user(
    email: EmailStr, password: str
) -> Optional[None | Users]:
    user = await UsersDAO.get_one_or_none(email=email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def create_acces_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ENCODE_ALGORITHM
    )
    return encoded_jwt


async def get_user_id_from_token(token: str) -> bool:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ENCODE_ALGORITHM
        )
    except JWTError:
        raise TokenException("error")
        # raise HTTPException(
        #     status_code=status.HTTP_401_UNAUTHORIZED,
        #     detail={'token_error': 'Неправильный токен авторизации!'}
        # )
    expire = payload.get("exp")
    if (not expire) or (int(expire)) < datetime.now().timestamp():
        raise TokenException("expired")
        # raise HTTPException(
        #     status_code=status.HTTP_401_UNAUTHORIZED,
        #     detail={'token_expired': 'Токен недействителен!'}
        # )
    user_id = payload.get("sub")
    if not user_id:
        raise TokenException("error")
    print(user_id, type(user_id))
    return int(user_id)
