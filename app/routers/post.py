from copy import deepcopy
from datetime import datetime
from typing import List
from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException, APIRouter

from app.classes.oauth2 import get_current_user
from app.classes.schemas.users import user_response

from ..classes.database import get_db
from ..classes.models import Post, User, posts, votes, users
from ..classes.schemas.posts import post_create, post_response, post_update


router = APIRouter(prefix="/posts", tags=['Posts'])


@router.get("", response_model=List[dict])
async def get_posts(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    res: List[post_response] = db.execute(
        posts.select().where(posts.c["user_id"] == user.id)).fetchall()

    if not res or len(res) == 0:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            "you don't added any posts yet")

    dict_res = []

    for i in res:
        count = db.query(func.count(votes.c.user_id)).where(
            votes.c.post_id == i.id).scalar()
        new_dict = dict(zip(i._fields, i.tuple()))
        new_dict["upvotes_count"] = count
        dict_res.append(new_dict)

    return dict_res


@router.post("", status_code=status.HTTP_201_CREATED, response_model=post_response)
async def create_post(post: post_create, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    # TODO auto mapping
    temp_dict = post.dict()
    temp_dict.update({"created_at": datetime.now()})
    temp_dict.update({"user_id": user.id})
    new_post = Post(**temp_dict)
    temp_dict.update({"creator": user})
    temp_dict.update({"upvotes_count": 0})
    temp_dict.update({"id": new_post.id})
    resp = post_response(**temp_dict)

    # db.add(Post(**new_post.dict()))
    posts.insert().values(**temp_dict)

    db.commit()
    # db.refresh(new_post)

    return new_post


@router.get("/latest", response_model=post_response)
async def get_latest_post(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    res = db.execute(posts.select().order_by(posts.c["created_at"]).where(
        posts.c["user_id"] == user.id)).fetchall()
    if res is None or len(res) == 0:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            "you don't added any posts yet")
    # reverse and taking the one
    res = res[::-1][0]

    return res


@router.get("/{id}", response_model=post_response)
async def get_post(id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    post = db.execute(posts.select().where(
        posts.c["user_id"] == user.id and posts.c["id"] == id)).fetchone()

    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"the {id}th post was not found")

    post_dict = dict(zip(post._fields, post.tuple()))
    post_dict.update({"creator": user_response(**user.__dict__)})

    return post_dict


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=post_response)
async def update_post(id: int, post: post_update, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    updated = db.execute(posts.select().where(
        posts.c["user_id"] == user.id and posts.c["id"] == id)).fetchone()

    if updated == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"{id}th post was not found")

    new_dict = dict(zip(updated._fields, updated.tuple()))
    new_dict["created_at"] = None
    new_dict["title"] = post.title  # TODO auto mapping
    new_dict["content"] = post.content

    new_post = Post(**new_dict)

    db.delete(updated)

    db.add(new_post)
    db.refresh(new_post)
    db.commit()

    new_dict["creator"] = user_response(**user.__dict__)

    return new_dict


@router.delete("/{id}", status_code=204)
async def delete_post(id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    post = db.execute(posts.select().where(
        posts.c["user_id"] == user.id and posts.c["id"] == id)).fetchone()
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"{id}th post was not found")

    posts.delete().where(posts.c.id == id)

    db.commit()
    return
