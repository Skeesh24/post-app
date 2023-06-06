from typing import Optional
from sqlalchemy.orm import Session
from app.classes.database import get_db
from app.classes.models import User
from app.classes.schemas.tokens import token_data
from app.config import Config
from jose import JWTError
from jose.jwt import encode, decode
from datetime import datetime, timedelta
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    jwt = encode(to_encode, Config.JWT_SECRET_KEY, algorithm=Config.ALGORYTHM)

    return jwt


def verify_access_token(access_token: str, credentials_execption):
    try:
        payload = decode(access_token, Config.JWT_SECRET_KEY,
                         algorithms=Config.ALGORYTHM)

        id: Optional[str] = payload.get('user_id')

        if not id:
            raise credentials_execption
        # TODO auto mapping is needed
        data = token_data(id=id, created_at=datetime.now())

        return data
    except JWTError:
        raise credentials_execption


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could't validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"})

    data = verify_access_token(
        token, credentials_execption=credentials_exception)

    return db.get(User, data.id)
