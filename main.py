from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

note = APIRouter()

templates = Jinja2Templates(directory="templates")

db = MongoClient("mongodb://localhost:27017")

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    x = db.notes.notes.find({}) 
    for i in x:
        print(i)
    return templates.TemplateResponse("index.html", {"request": request})


@note.get("/items/{item_id}")
def read_item(item_id: int, q:str|None = None):
    return {"item_id": item_id, "q": q}

app.include_router(note)
