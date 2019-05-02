from __future__ import annotations
from typing import Dict, Any

import models
import app.errors as errors
import tools.uuid as uuid
import tools.validator as validator

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .main import Controller


async def notes_get(self: Controller, params: Dict[str, Any]) -> Dict[str, Any]:

    try:
        await validator.validate("notes_get", params)
    except validator.ValidationError:
        raise errors.InvalidParams

    try:
        note = await self.storage.get_note(params["id"])
    except errors.StorageException:
        raise errors.InternalError

    if not note.exists():
        raise errors.NoteNotFound

    result = {"id": note.get_id(), "title": note.get_title(), "data": note.get_data()}

    return result


async def notes_create(self: Controller, params: Dict[str, Any]) -> Dict[str, Any]:

    try:
        await validator.validate("notes_create", params)
    except validator.ValidationError:
        raise errors.InvalidParams

    note = models.Note(id_=await uuid.generate(), title=params["title"], data=params["data"])

    try:
        await self.storage.store_note(note)
    except errors.StorageException:
        raise errors.InternalError

    result = {"id": note.get_id()}

    return result


async def notes_update(self: Controller, params: Dict[str, Any]) -> Dict[str, Any]:

    try:
        await validator.validate("notes_update", params)
    except validator.ValidationError:
        raise errors.InvalidParams

    try:
        note = await self.storage.get_note(params["id"])
    except errors.StorageException:
        raise errors.InternalError

    if not note.exists():
        raise errors.NoteNotFound

    if "title" in params:
        note.set_title(params["title"])

    if "data" in params:
        note.set_data(params["data"])

    try:
        await self.storage.update_note(note)
    except errors.StorageException:
        raise errors.InternalError

    result = {}

    return result


async def notes_delete(self: Controller, params: Dict[str, Any]) -> Dict[str, Any]:

    try:
        await validator.validate("notes_delete", params)
    except validator.ValidationError:
        raise errors.InvalidParams

    try:
        note = await self.storage.get_note(params["id"])
    except errors.StorageException:
        raise errors.InternalError

    if not note.exists():
        raise errors.NoteNotFound

    try:
        await self.storage.delete_note(note)
    except errors.StorageException:
        raise errors.InternalError

    result = {}

    return result
