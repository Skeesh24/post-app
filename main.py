from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


temp_storage = [{"title": "title of post 1",
                 "content": "content of post 1", "id": 1},
                {"title": "favourite foods", "content": "I like pizza", "id": 2}]


app = FastAPI()


@app.get("/")
async def root():
    return {"message ": "welcome to my api"}


@app.get("/posts")
async def get_posts():
    return {"data": temp_storage}


@app.post("/posts")
async def create_post(post: Post):
    return {"data": post.__dict__}
