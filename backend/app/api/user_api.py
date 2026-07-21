from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.user_schemas import (
    UserCreate,
    UserUpdate,
    UserResponse
)

from app.services.user_service import UserService


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# ----------------------------
# Create User
# ----------------------------

@router.post(
    "/",
    response_model=UserResponse,
    status_code=201
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    return UserService.create_user(
        db,
        user
    )


# ----------------------------
# Get All Users
# ----------------------------

@router.get(
    "/",
    response_model=List[UserResponse]
)
def get_users(
    db: Session = Depends(get_db)
):

    return UserService.get_users(
        db
    )


# ----------------------------
# Get User By ID
# ----------------------------

@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    return UserService.get_user_by_id(
        db,
        user_id
    )


# ----------------------------
# Update User
# ----------------------------

@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):

    return UserService.update_user(
        db,
        user_id,
        user
    )


# ----------------------------
# Deactivate User
# ----------------------------

@router.delete(
    "/{user_id}"
)
def deactivate_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = UserService.deactivate_user(
        db,
        user_id
    )

    return {
        "message": "User deactivated successfully",
        "user_id": user.id,
        "is_active": user.is_active
    }