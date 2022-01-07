#import fastapi

from typing import Optional
from fastapi import FastAPI
import fastapi

#import  server
import uvicorn

#create api opbject isntance of the api
api = FastAPI()

#home page

api.get('/')
# ther ref pertains to paths within the 
def index() :
    body = "<html>" \
            "<body style = 'padding: 10px;'>"\
            "<h1>Welcome to the Amazing API</h1>"\
            "<div>"\
            "Try it: <a href='/api/calculate?x=7&y=11'>/api/calculate?x=7&y=11</a>"\
            "</div>"\
            "</body>"\
            "</html>"
            
    return fastapi.responses.HTMLResponse(content=body)

#endpoint use app to decorate the  function
@api.get("/api/calculate")
#the variable taken by the  get, post,...functions are actually the query parameters of our api
#default value then we must not pass it and instead of writing them int he query string we could 
#moidify the the  route into @api.get("/api/calculate/{x}/{y}")
def calculate(x : int ,y : int,z: Optional[int] = None ):
    value= (x+y)
    #bad request so we don't want our server break  but that they have  made a bad request
    #can do this sot that  even our responses are json to keep a consitent format
    if z == 0:
        return fastapi.responses.JSONResponse(content= {"error":"ERROR: Z cannot be zero."}, status_code=400)
        
    if z is not None:
        value /=z
    return {
        'value':value
}
    
#in flask we would add the following line
#api.run but here we provide an external server that will host our api and render it for use (local)
#but in fastapi comes with an integratede production ready server  which can host our api
#fastapi handles a lot for us
uvicorn.run(api, port = 8000, host = "127.0.0.1")


#this is the concept  for a minimal API endpoint