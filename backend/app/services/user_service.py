from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.repositories.user_repository import UserRepository
from app.schemas.user_schemas import UserCreate, UserUpdate


class UserService:

    # ---------------------------------
    # Create User
    # ---------------------------------

    @staticmethod
    def create_user(
        db: Session,
        user: UserCreate
    ):
        normalized_email = str(user.email).strip().lower()

        existing_user = UserRepository.get_by_email(
            db,
            normalized_email
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        if not user.name.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Name cannot be empty"
            )

        user.email = normalized_email
        user.password = hash_password(user.password)

        return UserRepository.create(
            db,
            user
        )


    # ---------------------------------
    # Get User By ID
    # ---------------------------------

    @staticmethod
    def get_user_by_id(
        db: Session,
        user_id: int
    ):
        user = UserRepository.get_by_id(
            db,
            user_id
        )

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return user


    # ---------------------------------
    # Get All Users
    # ---------------------------------

    @staticmethod
    def get_users(
        db: Session,
        skip: int = 0,
        limit: int = 10
    ):
        return UserRepository.get_all(
            db,
            skip,
            limit
        )


    # ---------------------------------
    # Update User
    # ---------------------------------

    @staticmethod
    def update_user(
        db: Session,
        user_id: int,
        user_data: UserUpdate
    ):
        existing_user = UserRepository.get_by_id(
            db,
            user_id
        )

        if existing_user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        if user_data.name is not None:
            user_data.name = user_data.name.strip()

            if not user_data.name:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Name cannot be empty"
                )

        if user_data.email is not None:
            normalized_email = str(
                user_data.email
            ).strip().lower()

            if normalized_email != existing_user.email:
                email_owner = UserRepository.get_by_email(
                    db,
                    normalized_email
                )

                if email_owner is not None:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Email already registered"
                    )

            user_data.email = normalized_email

        if user_data.password is not None:
            user_data.password = hash_password(
                user_data.password
            )

        return UserRepository.update(
            db,
            existing_user,
            user_data
        )


    # ---------------------------------
    # Deactivate User
    # ---------------------------------

    @staticmethod
    def deactivate_user(
        db: Session,
        user_id: int
    ):
        existing_user = UserRepository.get_by_id(
            db,
            user_id
        )

        if existing_user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return UserRepository.deactivate(
            db,
            existing_user
        )


    # ---------------------------------
    # Activate User
    # ---------------------------------

    @staticmethod
    def activate_user(
        db: Session,
        user_id: int
    ):
        existing_user = UserRepository.get_by_id(
            db,
            user_id
        )

        if existing_user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return UserRepository.activate(
            db,
            existing_user
        )