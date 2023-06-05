from pydantic import BaseModel, EmailStr
from datetime import datetime


class PostValidationBase(BaseModel):
    title: str
    content: str
    published: bool = True

    class Config:
        orm_mode = True


class PostCreate(PostValidationBase):
    pass


class PostUpdate(PostValidationBase):
    pass


class PostResponse(PostValidationBase):
    id: int
    created_at: datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(UserCreate):
    pass


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
