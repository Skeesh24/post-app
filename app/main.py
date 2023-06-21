from fastapi import FastAPI

from .routers.post import router as post_router
from .routers.user import router as user_router
from .routers.auth import router as auth_router
from .routers.vote import router as vote_router
from config import Settings
from uvicorn import run


app = FastAPI()
app.include_router(post_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(vote_router)


run(app, port=Settings.SERVER_PORT)


@app.get("/")
async def root():
    return {"message ": "welcome post-app"}
