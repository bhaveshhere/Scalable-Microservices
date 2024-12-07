from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic model for Post
class Post(BaseModel):
    username: str
    content: str

posts_db = []

@app.post("/posts/")
def create_post(post: Post):
    posts_db.append(post)
    return {"message": "Post created", "post": post}

@app.get("/posts/")
def get_posts() -> List[Post]:
    return posts_db

@app.get("/posts/{username}")
def get_user_posts(username: str) -> List[Post]:
    user_posts = [post for post in posts_db if post.username == username]
    return user_posts
