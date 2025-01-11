from sqlalchemy import JSON, Column, Computed, Date, Float, ForeignKey, Integer, String
from app.database import Base


class Bookings(Base):

    room_id = (ForeignKey('rooms.id'))
    user_id = (ForeignKey('user.id'))
    date_from = Column(Date, nullable=False)
    date_to =Column(Date, nullable=False)
    price = Column(Integer)
    total_cost = Column(Integer, Computed('(date_from - date_to) *price'))
    total_days = Column(Integer, Computed('date_from - date_to'))
