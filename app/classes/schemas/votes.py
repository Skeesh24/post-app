
from datetime import datetime
from pydantic import BaseModel, EmailStr, conint


class vote_create(BaseModel):
    post_id: int
    vote_direction: conint(ge=0, lt=2)


class vote_update(vote_create):
    pass


class vote_response(vote_create):

    class Config:
        orm_mode = True
