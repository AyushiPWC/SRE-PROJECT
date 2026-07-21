from typing import List

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user

from app.models.user import User

from app.schemas.booking_schema import (
    BookingCreate,
    BookingResponse,
    BookingStatusUpdate
)

from app.services.booking_service import BookingService
from app.repositories.booking_repository import BookingRepository


router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


# ==========================================
# Create Booking
# ==========================================

@router.post(
    "/",
    response_model=BookingResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Booking"
)
def create_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return BookingService.create_booking(
        db=db,
        user_id=current_user.id,
        booking=booking
    )


# ==========================================
# Get Logged-in User Bookings
# ==========================================

@router.get(
    "/my-bookings",
    response_model=List[BookingResponse],
    summary="Get My Bookings"
)
def get_my_bookings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return BookingRepository.get_user_bookings(
        db,
        current_user.id
    )


# ==========================================
# Get Hotel Bookings
# ==========================================

@router.get(
    "/hotel/{hotel_id}",
    response_model=List[BookingResponse],
    summary="Get Hotel Bookings"
)
def get_hotel_bookings(
    hotel_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return BookingRepository.get_hotel_bookings(
        db,
        hotel_id
    )


# ==========================================
# Get Booking By ID
# ==========================================

@router.get(
    "/{booking_id}",
    response_model=BookingResponse,
    summary="Get Booking"
)
def get_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    booking = BookingRepository.get_by_id(
        db,
        booking_id
    )

    if booking is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )

    return booking


# ==========================================
# Update Booking Status
# ==========================================

@router.put(
    "/{booking_id}/status",
    response_model=BookingResponse,
    summary="Update Booking Status"
)
def update_booking_status(
    booking_id: int,
    status_update: BookingStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return BookingService.update_booking_status(
        db,
        booking_id,
        status_update
    )


# ==========================================
# Cancel Booking
# ==========================================

@router.put(
    "/{booking_id}/cancel",
    response_model=BookingResponse,
    summary="Cancel Booking"
)
def cancel_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return BookingService.cancel_booking(
        db,
        booking_id
    )