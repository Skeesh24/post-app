from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


temp_storage = [{"title": "default title",
                 "content": "default content", "id": 1}]


def find_post(id: int):
    for post in temp_storage:
        if post["id"] == id:
            return post


app = FastAPI()


@app.get("/")
async def root():
    return {"message ": "welcome to my api"}


@app.get("/posts")
async def get_posts():
    return {"data": temp_storage}


@ app.post("/posts")
async def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    temp_storage.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/latest")
async def get_latest_post():
    post = temp_storage[len(temp_storage)-1]
    return {"detail": post}


@app.get("/posts/{id}")
async def get_post(id: int):
    post = find_post(id)
    return {"data": post}
