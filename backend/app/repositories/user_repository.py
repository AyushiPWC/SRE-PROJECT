from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    @staticmethod
    def get_by_email(
        db: Session,
        email: str
    ) -> Optional[User]:

        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )


    @staticmethod
    def get_by_id(
        db: Session,
        user_id: int
    ) -> Optional[User]:

        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )


    @staticmethod
    def get_all(
        db: Session,
        skip: int = 0,
        limit: int = 10
    ) -> List[User]:

        return (
            db.query(User)
            .order_by(User.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )


    @staticmethod
    def create(
        db: Session,
        user
    ) -> User:

        db_user = User(
            name=user.name,
            email=str(user.email).strip().lower(),
            password=user.password,
            is_active=True
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user


    @staticmethod
    def update(
        db: Session,
        db_user: User,
        user_update
    ) -> User:

        if user_update.name is not None:
            db_user.name = user_update.name.strip()

        if user_update.email is not None:
            db_user.email = (
                str(user_update.email)
                .strip()
                .lower()
            )

        if user_update.password is not None:
            db_user.password = user_update.password

        db.commit()
        db.refresh(db_user)

        return db_user


    @staticmethod
    def deactivate(
        db: Session,
        db_user: User
    ) -> User:

        db_user.is_active = False

        db.commit()
        db.refresh(db_user)

        return db_user


    @staticmethod
    def activate(
        db: Session,
        db_user: User
    ) -> User:

        db_user.is_active = True

        db.commit()
        db.refresh(db_user)

        return db_user