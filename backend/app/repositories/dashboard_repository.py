from datetime import date

from sqlalchemy.orm import Session

from app.models.booking import Booking

from app.core.enums import BookingStatus



class DashboardRepository:


    @staticmethod
    def get_user_dashboard(
        db: Session,
        user_id: int
    ):


        total_bookings = (

            db.query(Booking)

            .filter(
                Booking.user_id == user_id
            )

            .count()

        )



        confirmed_bookings = (

            db.query(Booking)

            .filter(

                Booking.user_id == user_id,

                Booking.status ==
                BookingStatus.CONFIRMED.value

            )

            .count()

        )



        cancelled_bookings = (

            db.query(Booking)

            .filter(

                Booking.user_id == user_id,

                Booking.status ==
                BookingStatus.CANCELLED.value

            )

            .count()

        )



        upcoming_bookings = (

            db.query(Booking)

            .filter(

                Booking.user_id == user_id,

                Booking.check_in_date >= date.today()

            )

            .count()

        )



        return {


            "total_bookings":
                total_bookings,


            "confirmed_bookings":
                confirmed_bookings,


            "cancelled_bookings":
                cancelled_bookings,


            "upcoming_bookings":
                upcoming_bookings

        }