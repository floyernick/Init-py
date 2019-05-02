from __future__ import annotations

import models
import app.errors as errors
import tools.logger as logger

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .main import Storage


async def get_note(self: Storage, id_: str) -> models.Note:

    note = models.Note()

    query = "SELECT id, title, data FROM notes WHERE id = $1"

    try:
        result = await self.performer().fetchrow(query, id_)
    except Exception as e:
        await logger.warning(e)
        raise errors.StorageException

    if result is None:
        return note

    note.set_id(str(result["id"]))
    note.set_title(result["title"])
    note.set_data(result["data"])

    return note


async def store_note(self: Storage, note: models.Note) -> None:

    query = "INSERT INTO notes(id, title, data) VALUES ($1, $2, $3)"

    try:
        await self.performer().execute(query, note.get_id(), note.get_title(), note.get_data())
    except Exception as e:
        await logger.warning(e)
        raise errors.StorageException


async def update_note(self: Storage, note: models.Note) -> None:

    query = "UPDATE notes SET title = $2, data = $3 WHERE id = $1"

    try:
        await self.performer().execute(query, note.get_id(), note.get_title(), note.get_data())
    except Exception as e:
        await logger.warning(e)
        raise errors.StorageException


async def delete_note(self: Storage, note: models.Note) -> None:

    query = "DELETE FROM notes WHERE id = $1"

    try:
        await self.performer().execute(query, note.get_id())
    except Exception as e:
        await logger.warning(e)
        raise errors.StorageException
