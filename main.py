from fastapi import FastAPI   #import
from typing import Optional
from pydantic import BaseModel
import uvicorn

app =FastAPI()   #instance of API 

@app.get('/blog')   # this means decorator and '/' means base url localhost8000
def index(limit=10, published: bool=True, sort:Optional[str]=None):       #function
    if published:
            return {'data':f'{limit} published  blogs from the db'}
    else:
            return {'data':f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():             #function
    #fetch blog with id =id
    return {'data': 'all unpublished blogs'} 

@app.get('/blog?limit=10&published=True')
def index():             #function
    #fetch blog with id =id
    return {'data': 'blog list'} 

@app.get('/blog/{id}')
def show(id : int):             #function
    #fetch blog with id =id

    return {'data': id} 

@app.get('/blog/{id}/comments')
def comments(id, limit=10):             #function
    #fetch blog with id =id
    return {'data': {'1', '2'}} 
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
        
@app.post('/blog')
def create_blog(blog: Blog):

    return{'data': "Blog is created with title as {blog.title}"}

# if __name__=="__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)