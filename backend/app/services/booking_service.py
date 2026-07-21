from datetime import date

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.booking_repository import BookingRepository
from app.repositories.hotel_repository import HotelRepository
from app.repositories.user_repository import UserRepository

from app.schemas.booking_schema import (
    BookingCreate,
    BookingStatusUpdate
)

from app.core.enums import (
    BookingStatus,
    BOOKING_STATUS_TRANSITIONS
)



class BookingService:


    # ---------------------------------
    # Create Booking
    # ---------------------------------

    @staticmethod
    def create_booking(
        db: Session,
        user_id: int,
        booking: BookingCreate
    ):


        # Validate User

        user = UserRepository.get_by_id(
            db,
            user_id
        )


        if not user:

            raise HTTPException(
                status_code=404,
                detail="User not found"
            )



        # Validate Hotel

        hotel = HotelRepository.get_by_id(
            db,
            booking.hotel_id
        )


        if not hotel:

            raise HTTPException(
                status_code=404,
                detail="Hotel not found or inactive"
            )



        # Validate Dates

        today = date.today()


        if booking.check_in_date < today:

            raise HTTPException(
                status_code=400,
                detail="Check-in date cannot be in the past"
            )


        if booking.check_out_date <= booking.check_in_date:

            raise HTTPException(
                status_code=400,
                detail="Check-out date must be after check-in date"
            )



        nights = (
            booking.check_out_date -
            booking.check_in_date
        ).days



        if nights < 1:

            raise HTTPException(
                status_code=400,
                detail="Minimum stay should be 1 night"
            )



        # Availability Check

        overlapping = BookingRepository.has_overlapping_booking(
            db,
            booking.hotel_id,
            booking.check_in_date,
            booking.check_out_date
        )


        if overlapping:

            raise HTTPException(
                status_code=400,
                detail="Hotel unavailable for selected dates"
            )



        # Calculate Total Price

        total_price = (
            hotel.price_per_night *
            nights
        )



        return BookingRepository.create(

            db=db,

            user_id=user_id,

            booking=booking,

            total_price=total_price

        )



    # ---------------------------------
    # Cancel Booking
    # ---------------------------------

    @staticmethod
    def cancel_booking(
        db: Session,
        booking_id: int
    ):


        booking = BookingRepository.get_by_id(
            db,
            booking_id
        )


        if not booking:

            raise HTTPException(
                status_code=404,
                detail="Booking not found"
            )



        if booking.status in [

            BookingStatus.CHECKED_OUT.value,

            BookingStatus.CANCELLED.value

        ]:

            raise HTTPException(
                status_code=400,
                detail="Booking cannot be cancelled"
            )



        return BookingRepository.cancel_booking(
            db,
            booking_id
        )



    # ---------------------------------
    # Update Booking Status
    # ---------------------------------

    @staticmethod
    def update_booking_status(
        db: Session,
        booking_id: int,
        status_update: BookingStatusUpdate
    ):


        booking = BookingRepository.get_by_id(
            db,
            booking_id
        )


        if not booking:

            raise HTTPException(
                status_code=404,
                detail="Booking not found"
            )



        current_status = booking.status

        new_status = status_update.status



        if new_status not in BOOKING_STATUS_TRANSITIONS[current_status]:

            raise HTTPException(
                status_code=400,
                detail=(
                    f"Cannot change booking "
                    f"from {current_status} "
                    f"to {new_status}"
                )
            )



        return BookingRepository.update_status(
            db,
            booking_id,
            BookingStatus(new_status)
        )