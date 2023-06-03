from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message ": "welcome to my api"}


@app.get("posts/")
async def get_posts():
    return {"data": "This is ur posts"}


@app.post("/createpost")
async def create_post(post: Post):
    return post.__dict__
