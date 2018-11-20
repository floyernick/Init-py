from typing import Dict

import models
import tools.uuid as uuid
import tools.validator as validator


async def notes_get(self, req: Dict) -> Dict:

    if not await validator.validate("notes_get", req):
        raise Exception("invalid params")

    try:
        note = await self.db.get_note(req["note_id"])
    except Exception as _:
        raise Exception("internal error")

    if note.id == uuid.NIL_UUID:
        raise Exception("invalid note id")

    res = {
        "note_id": note.id,
        "note_title": note.title,
        "note_data": note.data
    }

    return res


async def notes_create(self, req: Dict) -> Dict:

    if not await validator.validate("notes_create", req):
        raise Exception("invalid params")

    note = models.Note(
        id=uuid.generate(), title=req["note_title"], data=req["note_data"])

    try:
        await self.db.store_note(note)
    except Exception as _:
        raise Exception("internal error")

    res = {"id": note.id}

    return res


async def notes_update(self, req: Dict) -> Dict:

    if not await validator.validate("notes_update", req):
        raise Exception("invalid params")

    try:
        note = await self.db.get_note(req["note_id"])
    except Exception as _:
        raise Exception("internal error")

    note.title = req["note_title"]
    note.data = req["note_data"]

    try:
        await self.db.update_note(note)
    except Exception as _:
        raise Exception("internal error")

    res = {"id": note.id}

    return res


async def notes_delete(self, req: Dict) -> Dict:

    if not await validator.validate("notes_delete", req):
        raise Exception("invalid params")

    try:
        note = await self.db.get_note(req["note_id"])
    except Exception as _:
        raise Exception("internal error")

    if note.id == uuid.NIL_UUID:
        raise Exception("invalid note id")

    try:
        await self.db.delete_note(note.id)
    except Exception as _:
        raise Exception("internal error")

    res = {}

    return res
