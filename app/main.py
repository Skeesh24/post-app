from fastapi import FastAPI, status, HTTPException, Depends
from pydantic import BaseModel
from typing import Any, List, Optional
from fastapi import Response
from sqlalchemy.orm import Session
from sqlalchemy import DateTime, select
from datetime import datetime
from copy import deepcopy

from app.models import posts, metadata, Post
from .database import get_db, engine
from .schemas import PostResponse, PostCreate, PostUpdate


metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
async def root():
    return {"message ": "welcome to my api"}


@app.get("/posts")
async def get_posts(db: Session = Depends(get_db)):
    raw = db.execute(select(Post))
    len = db.execute(select(Post)).fetchall().__len__()

    res = []

    for i in range(len):
        res.append(Post.dictFromRow(raw.fetchone()))

    return {"data": res}


@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=List[PostResponse])
async def create_post(post: PostCreate, db: Session = Depends(get_db)):
    new_post = Post(**post.dict())

    db.add(new_post)

    db.commit()

    return new_post


@app.get("/posts/latest")
async def get_latest_post(db: Session = Depends(get_db)):
    sel = select(Post)
    res = list(db.execute(sel.order_by(
        posts.c["created_at"])).fetchall())
    # reverse and taking the one
    res = res[::-1][0]

    return {"detail": Post.dictFromRow(res)}


@app.get("/posts/{id}")
async def get_post(id: int, db: Session = Depends(get_db), response_model=PostResponse):
    post = db.get(Post, id)

    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"the {id}th post was not found")
    return {"data": post}


@app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=PostResponse)
async def update_post(id: int, post: PostUpdate, db: Session = Depends(get_db)):
    updated = db.get(Post, id)

    if updated == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"{id}th post was not found")

    new_post = deepcopy(updated)
    new_post.created_at = None
    new_post.title = updated.title
    new_post.content = updated.content

    db.delete(updated)

    db.add(new_post)

    db.commit()
    return {"data": updated}


@app.delete("/posts/{id}", status_code=204)
async def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.get(Post, id)

    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"{id}th post was not found")

    db.delete(post)

    db.commit()
    return
