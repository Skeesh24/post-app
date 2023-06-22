from fastapi import FastAPI
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware

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

app.include_router(post_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(vote_router)


# if __name__ == "__main__":
#     run("app.main:app", host=Config.SERVER_HOST,
#         port=Config.SERVER_PORT, log_level="info")
