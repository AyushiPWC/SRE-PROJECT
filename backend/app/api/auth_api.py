from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.user_schemas import (
    UserCreate,
    UserResponse
)

from app.services.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register User"
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return AuthService.register(db, user)


@router.post(
    "/login",
    summary="Login User"
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    access_token = AuthService.login(
        db=db,
        email=form_data.username,
        password=form_data.password
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }