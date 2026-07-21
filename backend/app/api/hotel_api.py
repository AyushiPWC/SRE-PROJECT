from typing import List

from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.hotel_schemas import (
    HotelCreate,
    HotelUpdate,
    HotelResponse
)

from app.services.hotel_service import HotelService



router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"]
)



# --------------------------------
# Create Hotel
# --------------------------------

@router.post(
    "/",
    response_model=HotelResponse,
    status_code=201
)
def create_hotel(
    hotel: HotelCreate,
    db: Session = Depends(get_db)
):

    return HotelService.create_hotel(
        db,
        hotel
    )



# --------------------------------
# Get All Hotels
# --------------------------------

@router.get(
    "/",
    response_model=List[HotelResponse]
)
def get_hotels(
    db: Session = Depends(get_db)
):

    return HotelService.get_hotels(
        db
    )



# --------------------------------
# Search Hotels
# --------------------------------

@router.get(
    "/search/{location}",
    response_model=List[HotelResponse]
)
def search_hotels(
    location:str,
    db:Session = Depends(get_db)
):

    return HotelService.search_hotels(
        db,
        location
    )



# --------------------------------
# Get Hotel By ID
# --------------------------------

@router.get(
    "/{hotel_id}",
    response_model=HotelResponse
)
def get_hotel(
    hotel_id:int,
    db:Session = Depends(get_db)
):

    return HotelService.get_hotel_by_id(
        db,
        hotel_id
    )



# --------------------------------
# Update Hotel
# --------------------------------

@router.put(
    "/{hotel_id}",
    response_model=HotelResponse
)
def update_hotel(
    hotel_id:int,
    hotel:HotelUpdate,
    db:Session = Depends(get_db)
):

    return HotelService.update_hotel(
        db,
        hotel_id,
        hotel
    )



# --------------------------------
# Deactivate Hotel
# --------------------------------

@router.delete(
    "/{hotel_id}"
)
def deactivate_hotel(
    hotel_id:int,
    db:Session = Depends(get_db)
):

    hotel = HotelService.deactivate_hotel(
        db,
        hotel_id
    )


    return {
        "message":"Hotel deactivated successfully",
        "hotel_id":hotel.id,
        "is_active":hotel.is_active
    }