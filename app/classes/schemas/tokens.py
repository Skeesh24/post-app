

from datetime import datetime
from pydantic import BaseModel


class token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode: True


class token_data(BaseModel):
    id: str
    created_at: datetime
