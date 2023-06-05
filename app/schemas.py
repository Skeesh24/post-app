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


class UserValidationBase(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class UserCreate(UserValidationBase):
    pass


class UserUpdate(UserValidationBase):
    pass


class UserResponse(UserValidationBase):
    id: int
    created_at: datetime
