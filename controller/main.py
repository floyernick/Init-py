from dataclasses import dataclass
from typing import Any

import storage
from . import notes


@dataclass
class Controller:

    storage: storage.Storage

    notes_get = notes.notes_get
    notes_create = notes.notes_create
    notes_update = notes.notes_update
    notes_delete = notes.notes_delete


async def init(storage_: Any) -> Controller:

    if not isinstance(storage_, storage.Storage):
        raise Exception("invalid storage instance")

    controller = Controller(storage_)

    return controller
