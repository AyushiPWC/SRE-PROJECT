from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.jwt import decode_access_token
from app.repositories.user_repository import UserRepository


# ==================================================
# Password hashing
# ==================================================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    """
    Convert a plain-text password into a secure hash.
    """

    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    """
    Compare a plain-text password with the stored hash.
    """

    try:
        return pwd_context.verify(
            plain_password,
            hashed_password
        )

    except (ValueError, TypeError):
        return False


# ==================================================
# OAuth2 bearer token
# ==================================================

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


# ==================================================
# Get authenticated user
# ==================================================

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={
            "WWW-Authenticate": "Bearer"
        }
    )

    payload = decode_access_token(token)

    if payload is None:
        raise credentials_exception

    user_id = payload.get("sub")

    if user_id is None:
        raise credentials_exception

    try:
        user_id = int(user_id)

    except (TypeError, ValueError):
        raise credentials_exception

    user = UserRepository.get_by_id(
        db,
        user_id
    )

    if user is None:
        raise credentials_exception

    if hasattr(user, "is_active") and not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )

    return user