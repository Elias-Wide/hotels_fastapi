from app.users.constants import ADMIN
from app.users.models import Users


def is_admin(user: Users) -> bool:
    if user.role == ADMIN:
        return True
    return False
