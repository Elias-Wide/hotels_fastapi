from app.users.constants import ADMIN
from app.users.exceptions import AccessDeniedException
from app.users.models import Users


def is_admin(user: Users) -> bool:
    """
    Проверка пользователя на наличие прав админа.
    Поднимает ошибку доступа, если для regular_user.
    """
    if user.role == ADMIN:
        return True
    raise AccessDeniedException()
