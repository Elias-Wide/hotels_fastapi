from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base
from app.hotels.models import Hotels


class Rooms(Base):
    hotel_id = Column(ForeignKey("hotels.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=True)
    quantity = Column(Integer, nullable=False)
    image_id = image_id = Column(Integer)
    hotel = relationship("Hotels", back_populates="rooms")
    booking = relationship("Bookings", back_populates="room")
