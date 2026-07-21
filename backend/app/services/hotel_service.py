from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.hotel_repository import HotelRepository

from app.schemas.hotel_schemas import (
    HotelCreate,
    HotelUpdate
)



class HotelService:


    # ---------------------------------
    # Create Hotel
    # ---------------------------------

    @staticmethod
    def create_hotel(
        db: Session,
        hotel: HotelCreate
    ):


        if hotel.price_per_night <= 0:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Price per night must be greater than zero"
            )



        if not hotel.name.strip():

            raise HTTPException(
                status_code=400,
                detail="Hotel name cannot be empty"
            )



        if not hotel.location.strip():

            raise HTTPException(
                status_code=400,
                detail="Hotel location cannot be empty"
            )



        return HotelRepository.create(
            db,
            hotel
        )



    # ---------------------------------
    # Get Hotels
    # ---------------------------------

    @staticmethod
    def get_hotels(
        db: Session,
        skip:int = 0,
        limit:int = 10
    ):


        return HotelRepository.get_all(
            db,
            skip,
            limit
        )



    # ---------------------------------
    # Get Hotel By ID
    # ---------------------------------

    @staticmethod
    def get_hotel_by_id(
        db:Session,
        hotel_id:int
    ):


        hotel = HotelRepository.get_by_id(
            db,
            hotel_id
        )


        if not hotel:

            raise HTTPException(
                status_code=404,
                detail="Hotel not found"
            )


        return hotel



    # ---------------------------------
    # Search Hotels
    # ---------------------------------

    @staticmethod
    def search_hotels(
        db:Session,
        location:str,
        skip:int = 0,
        limit:int = 10
    ):


        if not location.strip():

            raise HTTPException(
                status_code=400,
                detail="Location cannot be empty"
            )


        return HotelRepository.search_by_location(
            db,
            location,
            skip,
            limit
        )



    # ---------------------------------
    # Update Hotel
    # ---------------------------------

    @staticmethod
    def update_hotel(
        db:Session,
        hotel_id:int,
        hotel_data:HotelUpdate
    ):


        if (
            hotel_data.price_per_night is not None
            and hotel_data.price_per_night <= 0
        ):

            raise HTTPException(
                status_code=400,
                detail="Price must be greater than zero"
            )



        hotel = HotelRepository.update(
            db,
            hotel_id,
            hotel_data
        )



        if not hotel:

            raise HTTPException(
                status_code=404,
                detail="Hotel not found"
            )


        return hotel



    # ---------------------------------
    # Deactivate Hotel
    # ---------------------------------

    @staticmethod
    def deactivate_hotel(
        db:Session,
        hotel_id:int
    ):


        hotel = HotelRepository.deactivate(
            db,
            hotel_id
        )



        if not hotel:

            raise HTTPException(
                status_code=404,
                detail="Hotel not found"
            )


        return hotel



    # ---------------------------------
    # Activate Hotel
    # ---------------------------------

    @staticmethod
    def activate_hotel(
        db:Session,
        hotel_id:int
    ):


        hotel = HotelRepository.activate(
            db,
            hotel_id
        )



        if not hotel:

            raise HTTPException(
                status_code=404,
                detail="Hotel not found"
            )


        return hotel