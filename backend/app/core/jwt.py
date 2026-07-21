from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import JWTError, jwt

from app.core.config import settings


def create_access_token(
    data: dict,
    expires_delta: Optional[timedelta] = None
) -> str:

    payload = data.copy()

    expire = (
        datetime.now(timezone.utc) + expires_delta
        if expires_delta
        else datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    payload.update({
        "exp": expire
    })

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def decode_access_token(
    token: str
) -> Optional[dict]:

    try:
        return jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

    except JWTError:
        return None