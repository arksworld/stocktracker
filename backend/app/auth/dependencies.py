from jose import JWTError
from jose import jwt

from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        user_id = int(payload["sub"])

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )

    user = db.query(User).get(user_id)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found",
        )

    return user