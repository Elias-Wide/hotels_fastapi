from sqlalchemy import (
    Column,
    Computed,
    Date,
    ForeignKey,
    Integer,
)
from sqlalchemy.orm import relationship
from app.database import Base


class Bookings(Base):
    room_id = Column(ForeignKey("rooms.id"))
    user_id = Column(ForeignKey("users.id"))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer)
    total_cost = Column(Integer, Computed("(date_to - date_from) * price"))
    total_days = Column(Integer, Computed("date_to - date_from"))
    user = relationship("Users", back_populates="booking")
    room = relationship("Rooms", back_populates="booking")
