from app.users.models import Users


def is_admin(user: Users) - > bool:
    if user.role == 'admin':
        return True
    return False    