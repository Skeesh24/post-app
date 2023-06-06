from copy import deepcopy
from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException, APIRouter

from app.classes.oauth2 import get_current_user

from ..classes.database import get_db
from ..classes.models import Post, posts
from ..classes.schemas import post_create, post_response, post_update


router = APIRouter(prefix="/posts", tags=['Posts'])


@router.get("")
async def get_posts(db: Session = Depends(get_db)):
    raw = db.execute(select(Post))
    len = db.execute(select(Post)).fetchall().__len__()

    res: List[post_response] = []

    for i in range(len):
        res.append(Post.dictFromRow(raw.fetchone()))

    return {"data": res}  # TODO


@router.post("", status_code=status.HTTP_201_CREATED, response_model=post_response)
async def create_post(post: post_create, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    new_post = Post(**post.dict())

    db.add(new_post)

    db.commit()

    return new_post


@router.get("/latest", response_model=post_response)
async def get_latest_post(db: Session = Depends(get_db)):
    sel = select(Post)
    res = list(db.execute(sel.order_by(
        posts.c["created_at"])).fetchall())
    # reverse and taking the one
    res = res[::-1][0]

    return {"detail": Post.dictFromRow(res)}  # TODO


@router.get("/{id}", response_model=post_response)
async def get_post(id: int, db: Session = Depends(get_db)):
    post = db.get(Post, id)

    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"the {id}th post was not found")
    return {"data": post}  # TODO


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=post_response)
async def update_post(id: int, post: post_update, db: Session = Depends(get_db)):
    updated = db.get(Post, id)

    if updated == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"{id}th post was not found")

    new_post = deepcopy(updated)
    new_post.created_at = None
    new_post.title = updated.title  # TODO
    new_post.content = updated.content  # TODO

    db.delete(updated)

    db.add(new_post)

    db.commit()
    return {"data": updated}


@router.delete("/{id}", status_code=204)
async def delete_post(id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    print(user_id)
    post = db.get(Post, id)

    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"{id}th post was not found")

    db.delete(post)

    db.commit()
    return
