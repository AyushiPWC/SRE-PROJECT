from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


# ----------------------------
# Create User
# ----------------------------
class UserCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=100)


# ----------------------------
# Login User
# ----------------------------
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ----------------------------
# Update User
# ----------------------------
class UserUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=3, max_length=100)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(default=None, min_length=8, max_length=100)
    is_active: Optional[bool] = None


# ----------------------------
# User Response
# ----------------------------
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True