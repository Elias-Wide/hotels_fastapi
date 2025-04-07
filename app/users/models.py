from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType

from app.database import Base
from app.users.constants import USER_ROLE


class Users(Base):

    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    booking = relationship("Bookings", back_populates="user")
    role = Column(ChoiceType(USER_ROLE), default="regular_user")
