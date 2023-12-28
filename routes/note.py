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
    return templates.TemplateResponse("index.html", {"request": request, "notes":notes})


@note.post("/")
async def add_note(request: Request):
    formdata = await request.form()
    new_note = dict(formdata)
    new_note['important'] = True if 'important' in new_note.keys() else False
    new_note["_id"] = "1"
    x = conn.notes.notes.insert_one(new_note) 
    print(x)
    return {"success": True}


@note.put("/notes/{id}")
def read_item(id: int, q:str|None = None):
    if q is not None:
        conn.notes.notes.update_one({"_id" : str(id)}, {"update": "successful"})
        x = conn.notes.notes.find_one({"_id" : str(id)})
    print(x)
    return x

