from fastapi import FastAPI, status, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from fastapi import Response
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models import posts, metadata, Post
from .database import get_db, cursor, connection, engine


metadata.create_all(bind=engine)


class PostValid(BaseModel):
    title: str
    content: str
    published: bool = True


app = FastAPI()


@app.get("/")
async def root():
    return {"message ": "welcome to my api"}


@app.get("/posts")
async def get_posts(db: Session = Depends(get_db)):
    res = list(db.execute(select(Post)))
    l = [dict]

    for r in res:
        a = Post.dictFromRow(r)
        l.append(a)
    print(l[0])

    return {"data": l}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostValid, db: Session = Depends(get_db)):
    new_post = Post(**post.dict())

    db.add(new_post)

    db.commit()

    return {"data": new_post}


@app.get("/posts/latest")
async def get_latest_post(db: Session = Depends(get_db)):
    res = db.execute(select(Post).order_by(
        posts.c["id"]).limit(1)).fetchone()

    return {"detail": Post.dictFromRow(res)}


@app.get("/posts/{id}")
async def get_post(id: int, db: Session = Depends(get_db)):
    post = db.get(Post, id)

    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"the {id}th post was not found")
    return {"data": post}


@app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_post(id: int, post: PostValid):
    cursor.execute("""UPDATE "post-webapp".posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
                   (post.title, post.content, post.published, id,))
    updated = cursor.fetchone()

    connection.commit()

    if updated == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"{id}th post was not found")

    return {"data": updated}


@app.delete("/posts/{id}", status_code=204)
async def delete_post(id: int):
    cursor.execute(
        """DELETE FROM "post-webapp".posts WHERE id = %s RETURNING *""", (id,))
    post = cursor.fetchone()

    connection.commit()

    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"{id}th post was not found")
