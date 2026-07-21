from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.hotel import Hotel
from app.schemas.hotel_schemas import (
    HotelCreate,
    HotelUpdate
)


class HotelRepository:

    # --------------------------------
    # Create Hotel
    # --------------------------------

    @staticmethod
    def create(
        db: Session,
        hotel: HotelCreate
    ) -> Hotel:

        db_hotel = Hotel(
            name=hotel.name,
            location=hotel.location,
            description=hotel.description,
            price_per_night=hotel.price_per_night,
            available_rooms=hotel.available_rooms,
            rating=hotel.rating,
            image_url=hotel.image_url,
            is_active=True
        )

        db.add(db_hotel)
        db.commit()
        db.refresh(db_hotel)

        return db_hotel

    # --------------------------------
    # Get Active Hotels
    # --------------------------------

    @staticmethod
    def get_all(
        db: Session,
        skip: int = 0,
        limit: int = 10
    ) -> List[Hotel]:

        return (
            db.query(Hotel)
            .filter(
                Hotel.is_active.is_(True)
            )
            .order_by(
                Hotel.created_at.desc()
            )
            .offset(skip)
            .limit(limit)
            .all()
        )

    # --------------------------------
    # Search Hotel By Location
    # --------------------------------

    @staticmethod
    def search_by_location(
        db: Session,
        location: str,
        skip: int = 0,
        limit: int = 10
    ) -> List[Hotel]:

        return (
            db.query(Hotel)
            .filter(
                Hotel.location.ilike(f"%{location}%"),
                Hotel.is_active.is_(True)
            )
            .order_by(
                Hotel.price_per_night.asc()
            )
            .offset(skip)
            .limit(limit)
            .all()
        )

    # --------------------------------
    # Get Hotel By ID
    # --------------------------------

    @staticmethod
    def get_by_id(
        db: Session,
        hotel_id: int
    ) -> Optional[Hotel]:

        return (
            db.query(Hotel)
            .filter(
                Hotel.id == hotel_id,
                Hotel.is_active.is_(True)
            )
            .first()
        )

    # --------------------------------
    # Update Hotel
    # --------------------------------

    @staticmethod
    def update(
        db: Session,
        hotel_id: int,
        hotel_data: HotelUpdate
    ) -> Optional[Hotel]:

        hotel = (
            db.query(Hotel)
            .filter(
                Hotel.id == hotel_id
            )
            .first()
        )

        if not hotel:
            return None

        if hotel_data.name is not None:
            hotel.name = hotel_data.name

        if hotel_data.location is not None:
            hotel.location = hotel_data.location

        if hotel_data.description is not None:
            hotel.description = hotel_data.description

        if hotel_data.price_per_night is not None:
            hotel.price_per_night = hotel_data.price_per_night

        if hotel_data.available_rooms is not None:
            hotel.available_rooms = hotel_data.available_rooms

        if hotel_data.rating is not None:
            hotel.rating = hotel_data.rating

        if hotel_data.image_url is not None:
            hotel.image_url = hotel_data.image_url

        if hotel_data.is_active is not None:
            hotel.is_active = hotel_data.is_active

        db.commit()
        db.refresh(hotel)

        return hotel

    # --------------------------------
    # Soft Delete Hotel
    # --------------------------------

    @staticmethod
    def deactivate(
        db: Session,
        hotel_id: int
    ) -> Optional[Hotel]:

        hotel = (
            db.query(Hotel)
            .filter(
                Hotel.id == hotel_id
            )
            .first()
        )

        if not hotel:
            return None

        hotel.is_active = False

        db.commit()
        db.refresh(hotel)

        return hotel

    # --------------------------------
    # Restore Hotel
    # --------------------------------

    @staticmethod
    def activate(
        db: Session,
        hotel_id: int
    ) -> Optional[Hotel]:

        hotel = (
            db.query(Hotel)
            .filter(
                Hotel.id == hotel_id
            )
            .first()
        )

        if not hotel:
            return None

        hotel.is_active = True

        db.commit()
        db.refresh(hotel)

        return hotel

    # --------------------------------
    # Check Hotel Exists
    # --------------------------------

    @staticmethod
    def exists(
        db: Session,
        hotel_id: int
    ) -> bool:

        return (
            db.query(Hotel)
            .filter(
                Hotel.id == hotel_id,
                Hotel.is_active.is_(True)
            )
            .first()
            is not None
        )