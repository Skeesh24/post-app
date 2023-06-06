from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime


class post_validation_base(BaseModel):
    title: str
    content: str
    published: bool = True

    class Config:
        orm_mode = True


class post_create(post_validation_base):
    pass


class post_update(post_validation_base):
    pass


class post_response(post_validation_base):
    id: int
    created_at: datetime


class user_create(BaseModel):
    email: EmailStr
    password: str


class user_update(user_create):
    pass


class user_response(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class user_login(BaseModel):
    email: EmailStr
    password: str


class token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode: True


class token_data(BaseModel):
    id: str
    created_at: datetime
