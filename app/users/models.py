from sqlalchemy import Column, String
from app.database import Base


class Users(Base):

    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
