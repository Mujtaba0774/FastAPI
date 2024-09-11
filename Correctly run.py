from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body
from typing import Optional
from random import randrange
app = FastAPI()


class Post(BaseModel):
    title: str 
    content: str
    published: bool = True
    rating: Optional[int] = None
    
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id":1}, {"title": "favorite foodds", "content":"I like pizza","id":2}]
@app.get("/")
def read_root():
    return {"Greeting From Mujtaba"}


@app.get("/posts")
def get_posts():
    return {"data":"my_posts"}

@app.post("/posts")
def create_posts(post:Post):
    post_dict = post_dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.appent(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_posts(id):
    print(id)
    return {"post_detail":f"Here is post {id}"}  