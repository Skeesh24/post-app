from typing import Optional
from app.classes.schemas import Token_Data
from app.config import Config
from jose import JWTError
from jose.jwt import encode, decode
from datetime import datetime, timedelta
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


SECRET_KEY = Config.JWT_SECRET_KEY
ALGORYTHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORYTHM)

    return jwt


def verify_access_token(access_token: str, credentials_execption):
    try:
        payload = decode(access_token, SECRET_KEY, algorithms="HS256")

        id: Optional[int] = payload.get('user_id')

        if not id:
            raise credentials_execption

        token_data = Token_Data(id=id)

        return token_data
    except JWTError:
        raise credentials_execption


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could't validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"})

    return verify_access_token(token, credentials_execption=credentials_exception)
