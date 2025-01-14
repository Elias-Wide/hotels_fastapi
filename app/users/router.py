from fastapi import APIRouter, HTTPException, Response, status

from app.users.auth import (
    authenticate_user,
    create_acces_token,
    get_password_hash,
    verify_password,
)
from app.users.dao import UsersDAO
from app.users.schemas import SUserAuth, SUserCreate, SUserList


router = APIRouter(prefix="/auth", tags=["Регистрация и Аутентификация"])


@router.post("/register")
async def register(user_data: SUserCreate):
    user_exist = await UsersDAO.get_one_or_none(email=user_data.email)
    if user_exist:
        raise HTTPException(
            status_code=500,
            detail={"email_exist": "Пользователь с таким email уже зарегистрирован!"},
        )
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add_object(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"AUTH_ERROR": "Неверный email или пароль!"},
        )
    acces_token = create_acces_token({"sub": user.id})
    response.set_cookie("user_access_token", acces_token, httponly=True)
    return acces_token


@router.get("")
async def get_users() -> list[SUserList]:
    return await UsersDAO.find_all()
