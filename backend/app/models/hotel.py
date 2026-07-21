from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    Index
)

from sqlalchemy.orm import relationship

from app.core.database import Base


class Hotel(Base):

    __tablename__ = "hotels"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False,
        index=True
    )

    location = Column(
        String(100),
        nullable=False,
        index=True
    )

    description = Column(
        String(500),
        nullable=True
    )

    price_per_night = Column(
        Float,
        nullable=False
    )

    available_rooms = Column(
        Integer,
        default=10,
        nullable=False
    )

    rating = Column(
        Float,
        default=4.0,
        nullable=False
    )

    image_url = Column(
        String(500),
        nullable=True
    )

    is_active = Column(
        Boolean,
        default=True,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # ---------------------------------
    # Booking Relationship
    # ---------------------------------

    bookings = relationship(
        "Booking",
        back_populates="hotel"
    )

    # ---------------------------------
    # Database Indexes
    # ---------------------------------

    __table_args__ = (

        Index(
            "idx_hotel_location_price",
            "location",
            "price_per_night"
        ),

    )

    def __repr__(self):

        return (
            f"<Hotel("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"location='{self.location}', "
            f"price={self.price_per_night}, "
            f"rooms={self.available_rooms}, "
            f"rating={self.rating}, "
            f"is_active={self.is_active}"
            f")>"
        )