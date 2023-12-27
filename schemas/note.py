def noteEntity(note) -> dict:
    return {"id": str(note["_id"]),
            "title": note["title"],
            "desc": note["desc"],
            "important": note["important"],
            }


def notesEntity(notes) -> list:
    return [noteEntity(note) for note in notes]