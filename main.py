from fastapi import FastAPI, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
from fastapi import Response


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


temp_storage = [{"title": "default title",
                 "content": "default content", "id": 1}]


def find_post(id: int) -> dict | None:
    for post in temp_storage:
        if post["id"] == id:
            return post


def find_post_index(id: int) -> int | None:
    for i, post in enumerate(temp_storage):
        if post["id"] == id:
            return i
    return None


app = FastAPI()


@ app.get("/")
async def root():
    return {"message ": "welcome to my api"}


@ app.get("/posts")
async def get_posts():
    return {"data": temp_storage}


@ app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    temp_storage.append(post_dict)
    return {"data": post_dict}


@ app.get("/posts/latest")
async def get_latest_post():
    post = temp_storage[len(temp_storage)-1]
    return {"detail": post}


@ app.get("/posts/{id}")
async def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"the {id}th post was not found")
    return {"data": post}


@app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_post(id: int, post: Post):
    index = find_post_index(id)
    if index == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"{index}th post was not found")

    post_dict = post.dict()
    post_dict["id"] = id
    temp_storage[index] = post_dict
    return {"data": post_dict}


@app.delete("/posts/{id}", status_code=204)
async def delete_post(id: int):
    index = find_post_index(id)
    if not index:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"{id}th post was not found")
    temp_storage.pop(index)

    return
