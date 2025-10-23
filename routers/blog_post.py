from fastapi import APIRouter
from pydantic import BaseModel
from typing  import Optional

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class Blog_Model(BaseModel):
    title:str
    description:str
    nb_comments:int
    published:Optional[bool]
  

@router.post('/new')
def create_blog(blog:Blog_Model):
    return {'data':blog}

