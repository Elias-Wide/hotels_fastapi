from fastapi import status

from app.bookings.exceptions import BaseBookingException


class InValidDate(BaseBookingException):

    status_code = status.HTTP_400_BAD_REQUEST
    detail = {
        "invalid_date": "Дата заезда должна быть позже сегодняшней даты!"
    }


class DateFromCannotBeAfterDateTo(BaseBookingException):

    status_code = status.HTTP_400_BAD_REQUEST
    detail = {
        "invalid_date_from": "Дата заезда должна быть позже даты выезда!"
    }
