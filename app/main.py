from fastapi import FastAPI

from .routers.post import router as post_router
from .routers.user import router as user_router
from .routers.auth import router as auth_router
from .routers.vote import router as vote_router
from .config import Config
from uvicorn import run


app = FastAPI()
app.include_router(post_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(vote_router)


@app.get("/")
async def root():
    return {"message ": "welcome post-app"}


if __name__ == "__main__":
    run("app.main:app", host=Config.SERVER_HOST,
        port=Config.SERVER_PORT, log_level="info")
