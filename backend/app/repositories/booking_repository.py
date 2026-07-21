from typing import List, Optional
from datetime import date

from sqlalchemy.orm import Session

from app.models.booking import Booking
from app.schemas.booking_schema import BookingCreate

from app.core.enums import BookingStatus



class BookingRepository:


    # --------------------------------
    # Create Booking
    # --------------------------------

    @staticmethod
    def create(
        db: Session,
        user_id: int,
        booking: BookingCreate,
        total_price: float
    ) -> Booking:


        try:

            db_booking = Booking(

                user_id=user_id,

                hotel_id=booking.hotel_id,

                check_in_date=booking.check_in_date,

                check_out_date=booking.check_out_date,

                total_price=total_price,

                status=BookingStatus.CONFIRMED.value

            )


            db.add(db_booking)

            db.commit()

            db.refresh(db_booking)


            return db_booking


        except Exception:

            db.rollback()

            raise



    # --------------------------------
    # Get Booking By ID
    # --------------------------------

    @staticmethod
    def get_by_id(
        db: Session,
        booking_id: int
    ) -> Optional[Booking]:


        return (

            db.query(Booking)

            .filter(
                Booking.id == booking_id
            )

            .first()

        )



    # --------------------------------
    # Get All Bookings
    # --------------------------------

    @staticmethod
    def get_all(
        db: Session,
        skip: int = 0,
        limit: int = 10
    ) -> List[Booking]:


        return (

            db.query(Booking)

            .order_by(
                Booking.created_at.desc()
            )

            .offset(skip)

            .limit(limit)

            .all()

        )



    # --------------------------------
    # Get User Bookings
    # --------------------------------

    @staticmethod
    def get_user_bookings(
        db: Session,
        user_id: int
    ) -> List[Booking]:


        return (

            db.query(Booking)

            .filter(
                Booking.user_id == user_id
            )

            .order_by(
                Booking.created_at.desc()
            )

            .all()

        )



    # --------------------------------
    # Get Hotel Bookings
    # --------------------------------

    @staticmethod
    def get_hotel_bookings(
        db: Session,
        hotel_id: int
    ) -> List[Booking]:


        return (

            db.query(Booking)

            .filter(
                Booking.hotel_id == hotel_id
            )

            .order_by(
                Booking.created_at.desc()
            )

            .all()

        )



    # --------------------------------
    # Update Booking Status
    # --------------------------------

    @staticmethod
    def update_status(
        db: Session,
        booking_id: int,
        status: BookingStatus
    ) -> Optional[Booking]:


        booking = BookingRepository.get_by_id(
            db,
            booking_id
        )


        if not booking:

            return None



        try:

            booking.status = status.value


            db.commit()

            db.refresh(booking)


            return booking


        except Exception:

            db.rollback()

            raise



    # --------------------------------
    # Cancel Booking
    # --------------------------------

    @staticmethod
    def cancel_booking(
        db: Session,
        booking_id: int
    ) -> Optional[Booking]:


        return BookingRepository.update_status(

            db,

            booking_id,

            BookingStatus.CANCELLED

        )



    # --------------------------------
    # Check Availability
    # --------------------------------

    @staticmethod
    def has_overlapping_booking(
        db: Session,
        hotel_id: int,
        check_in_date: date,
        check_out_date: date
    ) -> bool:


        existing_booking = (

            db.query(Booking)

            .filter(

                Booking.hotel_id == hotel_id,


                Booking.status.in_(

                    [

                        BookingStatus.PENDING.value,

                        BookingStatus.CONFIRMED.value,

                        BookingStatus.CHECKED_IN.value

                    ]

                ),


                Booking.check_in_date < check_out_date,


                Booking.check_out_date > check_in_date

            )

            .first()

        )


        return existing_booking is not None