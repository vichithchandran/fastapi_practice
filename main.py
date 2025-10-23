from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get("/") #Path Parameters
def index():
    return {"message": "Hello, World!"}

# @app.get("/blog/all")
# def get_all_blogs():
#     return {"message": "All blogs Provided"}

@app.get("/blog/all" ,tags =['Blog'],
summary="Retrieve All Blogs",
description ="This API call simulates fetching all blogs.",
response_description = "The List of avaliable Blog"
) #Query Parameters
def get_all_blogs(page=1,page_size:Optional[int]=None):
    return {"message": f"All blogs provided with page {page} and page size {page_size}"}

@app.get("/blog/{id}/comments/{comment_id}", tags =['Blog','Comment']) #Path and Query Parameters
def get_comment(id:int,comment_id:int, valid: bool = True, username: Optional[str] = None):
    """ 
    Simulates retrieving a comment of a blog
    
    - **id** is mandatory path parameter
    - **comment_id** is mandatory path parameter
    - **valid** is a optional query parameter
    - **username** is a optional query parameter

    """
    return {"message": f"Blog post {id} and comment {comment_id} with valid {valid} and username {username}"}


class BlogType(str, Enum): #Enum Parameters
    short = "short"
    story = "story"
    howto = "howto"

# @app.get("/blog/type/{type}",tags =['Blog']) #Enum Parameters
# def get_blog_by_type(type: BlogType):
#     return {"message": f"Blog with type {type}"}

# class BlogCategory(Enum): #Enum Parameters
#     short = 1
#     story = 2
#     howto = 3

# @app.get("/blog/category/{category_id}",tags =['Blog']) #Enum Parameters
# def get_blog_by_category(category_id: int): #Dictionary Parameters
#     type_map ={
#         1: BlogType.short,
#         2: BlogType.story,
#         3: BlogType.howto,
#     }
#     blog_category= type_map.get(category_id) 
#     if blog_category:
#         return {"message": f"Blog with category {blog_category}"} 
#     else:
#         return {"message": f"Blog with category {category_id} not found"}


@app.get("/blog/{id}", status_code=status.HTTP_200_OK, tags =['Blog']) #Body Parameters
def get_blog(id: int, response : Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id {id}"}