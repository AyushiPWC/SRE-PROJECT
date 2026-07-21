from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Float,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Booking(Base):

    __tablename__ = "bookings"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    hotel_id = Column(
        Integer,
        ForeignKey("hotels.id"),
        nullable=False
    )


    check_in_date = Column(
        Date,
        nullable=False
    )


    check_out_date = Column(
        Date,
        nullable=False
    )


    total_price = Column(
        Float,
        nullable=False
    )


    status = Column(
        String,
        default="PENDING"
    )


    created_at = Column(
        DateTime,
        server_default=func.now()
    )


    # Relationships

    user = relationship(
        "User",
        back_populates="bookings"
    )


    hotel = relationship(
        "Hotel",
        back_populates="bookings"
    )