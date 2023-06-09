from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from app.classes.schemas.users import user_response


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
    user_id: int
    created_at: datetime
    creator: user_response
    upvotes_count: Optional[int]

    class Config:
        orm_mode = True
