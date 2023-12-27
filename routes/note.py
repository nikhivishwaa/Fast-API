from fastapi import APIRouter
from fastapi import Request, FastAPI
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity 
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    notes = []
    x = conn.notes.notes.find({}) 
    for i in x:
        notes.append(i)
        print(i)
    print(notes)
    return templates.TemplateResponse("index.html", {"request": request, "notes":notes})


# @note.get("/items/{item_id}")
# def read_item(item_id: int, q:str|None = None):
#     return {"item_id": item_id, "q": q}

# @note.post("/")
# def add_note(note: Note):
#     return noteEntity(note)