from fastapi import FastAPI
from uvicorn import run

from .classes.models import metadata
from .classes.database import engine
from .routers.post import router as post_router
from .routers.user import router as user_router


metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(post_router)
app.include_router(user_router)


@app.get("/")
async def root():
    return {"message ": "welcome to my api"}


# if __name__ == "__main__":
    # run(app=app, host=Config.SERVER_HOST, port=Config.SERVER_PORT)
