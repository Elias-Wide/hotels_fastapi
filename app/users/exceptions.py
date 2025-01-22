from fastapi import status

from app.bookings.exceptions import BaseBookingException


class UserExistException(BaseBookingException):

    status_code = status.HTTP_409_CONFLICT
    detail = {"user_exist": "Пользователь с таким email уже зарегистрирован!"}


class InCorrectEmailOrPassword(BaseBookingException):

    status_code = status.HTTP_409_CONFLICT
    detail = {"incorrect_auth_data": "Неверный email или пароль!"}


class TokenException(BaseBookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = {"auth_error": "Неверный токен!"}

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class TokenExpiredException(BaseBookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = {
        "expired": "Токен недействителен! Необходимо обновить токен",
    }

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class AccessDeniedException(BaseBookingException):

    status_code = status.HTTP_400_BAD_REQUEST
    detail = {"Access_Denied": "Необходимы права аднминистратора"}
