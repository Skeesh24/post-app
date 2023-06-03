from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message ": "welcome to my api"}


@app.get("posts/")
async def get_posts():
    return {"data": "This is ur posts"}
