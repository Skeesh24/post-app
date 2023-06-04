from fastapi import FastAPI, status, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from fastapi import Response
from sqlalchemy.orm import Session

from app.models import posts, metadata, Post
from .database import get_db, cursor, connection, engine


metadata.create_all(bind=engine)


class PostValid(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


app = FastAPI()


@ app.get("/")
async def root():
    return {"message ": "welcome to my api"}


@ app.get("/posts")
async def get_posts():
    cursor.execute("""SELECT * FROM "post-webapp".posts""")
    posts = cursor.fetchall()

    return {"data": posts}


@ app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostValid):
    new_post = cursor.execute(
        """INSERT INTO "post-webapp".posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))

    new_post = cursor.fetchone()

    connection.commit()

    return {"data": new_post}


@ app.get("/posts/latest")
async def get_latest_post():
    cursor.execute(
        """SELECT * FROM "post-webapp".posts ORDER BY created_at DESC LIMIT 1""")
    post = cursor.fetchone()
    return {"detail": post}


@ app.get("/posts/{id}")
async def get_post(id: int, db: Session = Depends(get_db)):
    cursor.execute(
        """SELECT * FROM "post-webapp".posts WHERE id = %s""", (id, ))
    post = cursor.fetchone()

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
