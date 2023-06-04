from pydantic import BaseModel
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
