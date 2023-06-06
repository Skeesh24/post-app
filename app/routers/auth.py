from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from app.classes.database import get_db
from app.classes.models import users
from app.classes.hashing import Hasher
from app.classes.oauth2 import create_access_token
from app.classes.schemas.tokens import token


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=token)
async def login(credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.execute(users.select().where(
        users.c["email"] == credentials.username)).fetchone()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="invalid credentials")

    hasher = Hasher()

    if not hasher.verify(credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="invalid credentials")

    access_token = create_access_token({"user_id": user.id})

    return token(access_token=access_token, token_type="Bearer")
