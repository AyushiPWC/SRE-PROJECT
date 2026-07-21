from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.jwt import create_access_token
from app.core.security import hash_password, verify_password
from app.repositories.user_repository import UserRepository


class AuthService:

    @staticmethod
    def register(
        db: Session,
        user
    ):
        user.email = user.email.strip().lower()

        existing_user = UserRepository.get_by_email(
            db,
            user.email
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        user.password = hash_password(
            user.password
        )

        return UserRepository.create(
            db,
            user
        )


    @staticmethod
    def login(
        db: Session,
        email: str,
        password: str
    ) -> str:

        email = email.strip().lower()

        db_user = UserRepository.get_by_email(
            db,
            email
        )

        if db_user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
                headers={
                    "WWW-Authenticate": "Bearer"
                }
            )

        if (
            hasattr(db_user, "is_active")
            and not db_user.is_active
        ):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User account is inactive"
            )

        password_is_valid = verify_password(
            password,
            db_user.password
        )

        if not password_is_valid:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
                headers={
                    "WWW-Authenticate": "Bearer"
                }
            )

        return create_access_token(
            data={
                "sub": str(db_user.id),
                "email": db_user.email
            }
        )