from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app=FastAPI()

templates =Jinja2Templates(directory = "templates")

@app.get("/",response_class=HTMLResponse)
def index(request:Request):
    context={"request":request}
    return templates.TemplateResponse("index.html", context)
@app.get("/sigin",response_class=HTMLResponse)
def sigin(request:Request):
    context={"request":request}
    return templates.TemplateResponse("Sigin.html", context)
