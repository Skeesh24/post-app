from app.config import Config
from jose import JWTError
from jose.jwt import encode
from datetime import datetime, timedelta


SECRET_KEY = Config.JWT_SECRET_KEY
ALGORYTHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORYTHM)

    return jwt
