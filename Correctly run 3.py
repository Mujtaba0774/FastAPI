from typing import Union

from fastapi import FastAPI, Response, status, HTTPException
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
    
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id":1}, 
            {"title": "favorite foodds", "content":"I like pizza","id":2}]

def find_posts(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_posts(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i
@app.get("/")
def root():
    return {"Greeting From Mujtaba"}

@app.get("/post")
def get_post():
    return {"data":"my_post"}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post_dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.appent(post_dict) 
    return {"data": post_dict} 
  
@app.get("/posts/{id}")
def get_posts(id:int, response:Response):
    post = find_posts(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'message:f,post with id: {id} was not found'}
    return {"post_detail":post}  

@app.delete("/posts/{id}")
def delete_post():
    # deleting post
    # find the index in the array that has required ID
    # my_posts.pop(index)
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/post/{id}")
def update_posts(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    post_dict = post_dict()
    post_dict["id"] = id
    my_posts[index] = post_dict
    return{"data":post_dict}