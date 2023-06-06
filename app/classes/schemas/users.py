
from datetime import datetime
from pydantic import BaseModel, EmailStr


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
