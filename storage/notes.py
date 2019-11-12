from __future__ import annotations
from typing import List

import models
import app.errors as errors
import tools.logger as logger

from . import interface, query_builder

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .main import Storage


class NoteQuery(interface.NoteQuery, query_builder.QueryBuilder):
    async def count(self) -> int:

        query = "SELECT COUNT(id) FROM notes"

        query = self._format_query(query, True)

        number = 0

        try:
            result = await self.storage.performer().fetchrow(query, *self.params)
        except Exception as e:
            await logger.warning(e)
            raise errors.StorageException

        if result is None:
            return number

        number = result["count"]

        return number

    async def fetch(self) -> List[models.Note]:

        notes = []

        query = "SELECT id, title, data FROM notes"

        query = self._format_query(query)

        try:
            results = await self.storage.performer().fetch(query, *self.params)
        except Exception as e:
            await logger.warning(e)
            raise errors.StorageException

        if results is None:
            return notes

        for result in results:
            note = models.Note()
            note.id = str(result["id"])
            note.title = result["title"]
            note.data = result["data"]
            notes.append(note)

        return notes

    async def fetch_one(self) -> models.Note:

        note = models.Note()

        query = "SELECT id, title, data FROM notes"

        query = self._format_query(query)

        try:
            result = await self.storage.performer().fetchrow(query, *self.params)
        except Exception as e:
            await logger.warning(e)
            raise errors.StorageException

        if result is None:
            return note

        note.id = str(result["id"])
        note.title = result["title"]
        note.data = result["data"]

        return note


async def get_notes(self: Storage) -> NoteQuery:
    return NoteQuery(self)


async def store_note(self: Storage, note: models.Note) -> None:

    query = "INSERT INTO notes(id, title, data) VALUES ($1, $2, $3)"

    try:
        await self.performer().execute(query, note.id, note.title, note.data)
    except Exception as e:
        await logger.warning(e)
        raise errors.StorageException


async def update_note(self: Storage, note: models.Note) -> None:

    query = "UPDATE notes SET title = $2, data = $3 WHERE id = $1"

    try:
        await self.performer().execute(query, note.id, note.title, note.data)
    except Exception as e:
        await logger.warning(e)
        raise errors.StorageException


async def delete_note(self: Storage, note: models.Note) -> None:

    query = "DELETE FROM notes WHERE id = $1"

    try:
        await self.performer().execute(query, note.id)
    except Exception as e:
        await logger.warning(e)
        raise errors.StorageException
