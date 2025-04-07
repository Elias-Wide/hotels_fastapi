from fastapi import HTTPException, status


class BaseBookingException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class RoomCantBeBooked(BaseBookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = {"booking_error": "Нет доступных комнат!"}
