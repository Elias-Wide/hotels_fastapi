from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.database import Base


class Users(Base):

    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    booking = relationship("Bookings", back_populates="user")
