from fastapi import APIRouter


router = APIRouter(prefix="/bookings", tags=["Бронирование"])


@router.get("")
def get_bookings():
    pass


@router.get("{/{booking_id}")
def get_bookings(booking_id: int):
    pass


# @router.get('')
# def get_bookings():
#     pass
