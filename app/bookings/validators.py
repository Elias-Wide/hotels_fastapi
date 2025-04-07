from datetime import datetime

from app.hotels.exceptions import InValidDate, DateFromCannotBeAfterDateTo


async def validate_date(date_from, date_to):
    if date_from >= date_to:
        raise DateFromCannotBeAfterDateTo()
    if date_to <= datetime.now().date():
        raise InValidDate()
