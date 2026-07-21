from enum import Enum


class BookingStatus(str, Enum):

    """
    Booking lifecycle status.

    Flow:

    PENDING
        |
        v
    CONFIRMED
        |
        v
    CHECKED_IN
        |
        v
    CHECKED_OUT


    Cancellation allowed from:
        PENDING
        CONFIRMED
    """

    PENDING = "PENDING"

    CONFIRMED = "CONFIRMED"

    CHECKED_IN = "CHECKED_IN"

    CHECKED_OUT = "CHECKED_OUT"

    CANCELLED = "CANCELLED"



# =====================================
# Allowed Booking Status Transitions
# =====================================

BOOKING_STATUS_TRANSITIONS = {


    BookingStatus.PENDING: [

        BookingStatus.CONFIRMED,

        BookingStatus.CANCELLED

    ],


    BookingStatus.CONFIRMED: [

        BookingStatus.CHECKED_IN,

        BookingStatus.CANCELLED

    ],


    BookingStatus.CHECKED_IN: [

        BookingStatus.CHECKED_OUT

    ],


    BookingStatus.CHECKED_OUT: [],


    BookingStatus.CANCELLED: []

}