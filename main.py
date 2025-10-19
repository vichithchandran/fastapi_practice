from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get("/") #Path Parameters
def index():
    return {"message": "Hello, World!"}

# @app.get("/blog/all")
# def get_all_blogs():
#     return {"message": "All blogs Provided"}

@app.get("/blog/all") #Query Parameters
def get_all_blogs(page=1,page_size:Optional[int]=None):
    return {"message": f"All blogs provided with page {page} and page size {page_size}"}

@app.get("/blog/{id}/comments/{comment_id}") #Path and Query Parameters
def get_comment(id:int,comment_id:int, valid: bool = True, username: Optional[str] = None):
    return {"message": f"Blog post {id} and comment {comment_id} with valid {valid} and username {username}"}


class BlogType(str, Enum): #Enum Parameters
    short = "short"
    story = "story"
    howto = "howto"

@app.get("/blog/type/{type}") #Enum Parameters
def get_blog_by_type(type: BlogType):
    return {"message": f"Blog with type {type}"}

class BlogCategory(Enum): #Enum Parameters
    short = 1
    story = 2
    howto = 3

@app.get("/blog/category/{category_id}") #Enum Parameters
def get_blog_by_category(category_id: int): #Dictionary Parameters
    type_map ={
        1: BlogType.short,
        2: BlogType.story,
        3: BlogType.howto,
    }
    blog_category= type_map.get(category_id) 
    if blog_category:
        return {"message": f"Blog with category {blog_category}"} 
    else:
        return {"message": f"Blog with category {category_id} not found"}


@app.get("/blog/{id}") #Body Parameters
def get_blog(id: int):
    return {"message": f"Blog with id {id}"}