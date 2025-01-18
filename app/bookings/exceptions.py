from fastapi import HTTPException, status


class RoomCantBeBooked(HTTPException):

    status_code = status.HTTP_409_CONFLICT
    detail = {"booking_error": "Нет доступных комнат!"}

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)
