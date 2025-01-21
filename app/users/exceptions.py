from fastapi import status

from app.bookings.exceptions import BaseBookingException


class UserExistException(BaseBookingException):

    status_code = status.HTTP_409_CONFLICT
    detail = {"USER_EXIST": "Пользователь с таким email уже зарегистрирован!"}


class InCorrectEmailOrPassword(BaseBookingException):

    status_code = status.HTTP_409_CONFLICT
    detail = {"AUTH_ERROR": "Неверный email или пароль!"}


class TokenException(BaseBookingException):
    errors = {
        "error": "Неверный токен",
        "expired": "Токен недействителен! Необходимо обновить токен",
    }

    def __init__(self, key="error"):
        super().__init__(status_code=self.status_code, detail=self.detail)
        self.detail = self.errors[key]


class AccessDeniedException(BaseBookingException):

    status = status.HTTP_400_BAD_REQUEST
    detail = {"Access_Denied": "Необходимы права аднминистратора"}
