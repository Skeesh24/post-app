from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from app.classes.schemas import UserLogin
from app.classes.database import get_db
from app.classes.models import users
from app.classes.hashing import Hasher


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
async def login(credentials: UserLogin, db: Session = Depends(get_db)):
    user = db.execute(users.select().where(
        users.c["email"] == credentials.email)).fetchone()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="invalid credentials")

    hasher = Hasher()

    if not hasher.verify(credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="invalid credentials")

    # create toker
    # return token
    return {"token": "== JWT =="}
