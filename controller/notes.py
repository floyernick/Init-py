from typing import Dict

import app
import models
import tools.uuid as uuid
import tools.validator as validator


async def notes_get(self, req: Dict) -> Dict:

    if not await validator.validate("notes_get", req):
        raise app.DomainException("invalid params")

    try:
        note = await self.storage.get_note(req["id"])
    except app.StorageException:
        raise app.DomainException("internal error")

    if note.id == uuid.NIL_UUID:
        raise app.DomainException("invalid note id")

    res = {"id": note.id, "title": note.title, "data": note.data}

    return res


async def notes_create(self, req: Dict) -> Dict:

    if not await validator.validate("notes_create", req):
        raise app.DomainException("invalid params")

    note = models.Note(
        id_=await uuid.generate(), title=req["title"], data=req["data"])

    try:
        await self.storage.store_note(note)
    except app.StorageException:
        raise app.DomainException("internal error")

    res = {"id": note.id}

    return res


async def notes_update(self, req: Dict) -> Dict:

    if not await validator.validate("notes_update", req):
        raise app.DomainException("invalid params")

    try:
        note = await self.storage.get_note(req["id"])
    except app.StorageException:
        raise app.DomainException("internal error")

    if "title" in req:
        note.title = req["title"]

    if "data" in req:
        note.data = req["data"]

    try:
        await self.storage.update_note(note)
    except app.StorageException:
        raise app.DomainException("internal error")

    res = {}

    return res


async def notes_delete(self, req: Dict) -> Dict:

    if not await validator.validate("notes_delete", req):
        raise app.DomainException("invalid params")

    try:
        note = await self.storage.get_note(req["id"])
    except app.StorageException:
        raise app.DomainException("internal error")

    if note.id == uuid.NIL_UUID:
        raise app.DomainException("invalid note id")

    try:
        await self.storage.delete_note(note.id)
    except app.StorageException:
        raise app.DomainException("internal error")

    res = {}

    return res
