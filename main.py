from fastapi import FastAPI
from fastapi.params import Body


app = FastAPI()


@app.get("/")
async def root():
    return {"message ": "welcome to my api"}


@app.get("posts/")
async def get_posts():
    return {"data": "This is ur posts"}


@app.post("/createpost")
async def create_post(payload: dict = Body(...)):
    return {"new post": f"title is '{payload['title']}', content is '{payload['content']}'"}
