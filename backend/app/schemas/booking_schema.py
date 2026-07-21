from pydantic import BaseModel, Field
from datetime import date



# ==========================================
# Create Booking Request
# ==========================================

class BookingCreate(BaseModel):

    hotel_id: int

    check_in_date: date

    check_out_date: date



# ==========================================
# Update Booking Status
# ==========================================

class BookingStatusUpdate(BaseModel):

    status: str = Field(
        ...,
        min_length=3
    )



# ==========================================
# Booking Response
# ==========================================

class BookingResponse(BaseModel):

    id: int

    user_id: int

    hotel_id: int

    check_in_date: date

    check_out_date: date

    total_price: float

    status: str



    class Config:

        from_attributes = True