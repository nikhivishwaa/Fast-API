from fastapi import APIRouter
from fastapi import Request, FastAPI
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity 
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated


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


@note.post("/")
async def add_note(request: Request):
    formdata = await request.form()
    print(formdata)
    # new_note = dict(formdata)
    # new_note['important'] = True if new_note['important'] == 'on' else False
    # print(new_note)
    # x = conn.notes.notes.insert_one(new_note) 
    x = conn.notes.notes.insert_one(dict(formdata)) 
    return {"success": True, "id":x}


# @note.get("/items/{item_id}")
# def read_item(item_id: int, q:str|None = None):
#     return {"item_id": item_id, "q": q}

