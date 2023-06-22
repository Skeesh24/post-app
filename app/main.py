from fastapi import Depends, FastAPI, HTTPException, status
from uvicorn import run
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app.classes.database import get_db
from app.classes.models import User
from app.classes.oauth2 import get_current_user
from app.classes.schemas.posts import post_response
from app.classes.schemas.users import user_response
from app.classes.schemas.votes import vote_create
from app.classes.models import posts, Vote, votes

from app.routers.post import router as post_router
from app.routers.user import router as user_router
from app.routers.auth import router as auth_router
from app.routers.vote import router as vote_router
from app.config import Config


app = FastAPI()


origins = [
    "https://post-app-eight.vercel.app",
    "http://127.0.0.1",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message ": "welcome post-app"}


@app.get("/latest", response_model=post_response)
async def get_latest_post(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    res = db.execute(posts.select().order_by(posts.c["created_at"]).where(
        posts.c["user_id"] == user.id)).fetchall()
    if res is None or len(res) == 0:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            "you don't added any posts yet")
    # reverse and taking the one
    res = res[::-1][0]

    post_dict = dict(zip(res._fields, res.tuple()))

    upvotes = db.execute(votes.select().where(
        votes.c.user_id == user.id).where(votes.c.post_id == res.id)).fetchall()

    post_dict.update({"creator": user_response(**user.__dict__)})
    post_dict.update({"upvotes_count": len(upvotes)})

    return post_dict

app.include_router(post_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(vote_router)


# if __name__ == "__main__":
#     run("app.main:app", host=Config.SERVER_HOST,
#         port=Config.SERVER_PORT, log_level="info")
