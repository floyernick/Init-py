from typing import Any

import storage
from . import notes


class Controller:
    def __init__(self, db: storage.Storage):
        self.db = db

    notes_get = notes.notes_get
    notes_create = notes.notes_create
    notes_update = notes.notes_update
    notes_delete = notes.notes_delete


async def init_controller(db: Any) -> Controller:

    if not isinstance(db, storage.Storage):
        raise Exception("invalid storage instance")

    controller = Controller(db)

    return controller
