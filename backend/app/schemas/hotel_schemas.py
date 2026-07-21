print("✅ LOADED UPDATED hotel_schemas.py")

from datetime import datetime
from typing import Optional

from pydantic import (
    BaseModel,
    Field
)


# --------------------------------
# Create Hotel Request
# --------------------------------

class HotelCreate(BaseModel):

    name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    location: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    description: Optional[str] = Field(
        default=None,
        max_length=500
    )

    price_per_night: float = Field(
        ...,
        gt=0
    )

    available_rooms: int = Field(
        default=10,
        ge=0
    )

    rating: float = Field(
        default=4.0,
        ge=0,
        le=5
    )

    image_url: Optional[str] = None


# --------------------------------
# Update Hotel Request
# --------------------------------

class HotelUpdate(BaseModel):

    name: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    location: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    description: Optional[str] = Field(
        default=None,
        max_length=500
    )

    price_per_night: Optional[float] = Field(
        default=None,
        gt=0
    )

    available_rooms: Optional[int] = Field(
        default=None,
        ge=0
    )

    rating: Optional[float] = Field(
        default=None,
        ge=0,
        le=5
    )

    image_url: Optional[str] = None

    is_active: Optional[bool] = None


# --------------------------------
# Hotel Response
# --------------------------------

class HotelResponse(BaseModel):

    id: int

    name: str

    location: str

    description: Optional[str]

    price_per_night: float

    available_rooms: int

    rating: float

    image_url: Optional[str]

    is_active: bool

    created_at: datetime

    updated_at: datetime

    class Config:

        from_attributes = True