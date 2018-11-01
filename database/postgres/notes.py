import asyncio
import logging

import models


async def get_note(self, id: str) -> models.Note:

    note = models.Note()

    query = "SELECT id, title, data FROM notes WHERE id = $1"

    try:
        result = await self.pool.fetchrow(query, id)
    except Exception as e:
        logging.error(e)
        raise

    if result is None:
        return note

    note.id = str(result["id"])
    note.title = result["title"]
    note.data = result["data"]

    return note


async def store_note(self, note: models.Note) -> None:

    query = "INSERT INTO notes(id, title, data) VALUES ($1, $2, $3)"

    try:
        await asyncio.shield(
            self.pool.execute(query, note.id, note.title, note.data))
    except Exception as e:
        logging.error(e)
        raise


async def update_note(self, note: models.Note) -> None:

    query = "UPDATE notes SET title = $2, data = $3 WHERE id = $1"

    try:
        await asyncio.shield(
            self.pool.execute(query, note.id, note.title, note.data))
    except Exception as e:
        logging.error(e)
        raise


async def delete_note(self, id: str) -> None:

    query = "DELETE FROM notes WHERE id = $1"

    try:
        await asyncio.shield(self.pool.execute(query, id))
    except Exception as e:
        logging.error(e)
        raise
