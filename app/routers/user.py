from fastapi import APIRouter, Depends, status, HTTPException
from classes.database import get_db
from classes.hashing import Hasher
from classes.models import User
from classes.schemas import UserCreate, UserResponse
from classes.hashing import Hasher
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/users", status_code=201, response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(**user.dict())

    # hashing the pass
    hasher = Hasher()
    new_user.password = hasher.get_hashed(new_user.password)

    db.add(new_user)

    db.commit()

    return new_user


@router.get("/users/{id}", response_model=UserResponse)
async def get_user(id: int, db: Session = Depends(get_db)):
    user = db.get(User, id)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"the {id}th user was not found")
    return user
