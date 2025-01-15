from fastapi import HTTPException, status


class UserExistException(HTTPException):

    status_code = status.HTTP_409_CONFLICT
    detail = {"USER_EXIST": "Пользователь с таким email уже зарегистрирован!"}

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class InCorrectEmailOrPassword(HTTPException):

    status_code = status.HTTP_409_CONFLICT
    detail = {'AUTH_ERROR": "Неверный email или пароль!'}

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class TokenException(HTTPException):
    errors = {
        "error": "Неверный токен",
        "expired": "Токен недействителен! Необходимо обновить токен",
    }
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = {"TOKEN_ERROR": "Ошибка токена аутентификации!"}

    def __init__(self, key="error"):
        super().__init__(status_code=self.status_code, detail=self.detail)
        self.detail = self.errors[key]
