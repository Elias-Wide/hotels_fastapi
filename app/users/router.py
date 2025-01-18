from fastapi import APIRouter, Depends, HTTPException, Response, status

from app.users.auth import (
    authenticate_user,
    create_acces_token,
    get_password_hash,
    verify_password,
)
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.exceptions import InCorrectEmailOrPassword, UserExistException
from app.users.models import Users
from app.users.schemas import SUserAuth, SUserCreate, SUserGet

router = APIRouter(prefix="/auth", tags=["Регистрация и Аутентификация"])


@router.post("/register")
async def register(user_data: SUserCreate):
    user_exist = await UsersDAO.get_one_or_none(email=user_data.email)
    if user_exist:
        raise UserExistException()
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add_object(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise InCorrectEmailOrPassword()
    acces_token = create_acces_token({"sub": str(user.id)})
    response.set_cookie("user_access_token", acces_token, httponly=True)
    return {"access_token": acces_token}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("user_access_token")


@router.get("/me")
async def get_user(
    current_user: Users = Depends(get_current_user),
) -> SUserGet:
    return current_user
