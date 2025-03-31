from fastapi import FastAPI   #import

app =FastAPI()   #instance of API 

@app. get('/')   # this means decorate and '/' means base url localhost8000

def index():       #function
    return {'data': {'name': 'Sheeba' }}

@app.get('/about')
def about():             #function
    return {'data': 'about page'}