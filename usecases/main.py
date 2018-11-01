from typing import Any

import database
from . import notes


class Controller:
    def __init__(self, db: database.Database):
        self.db = db

    notes_get = notes.notes_get
    notes_create = notes.notes_create
    notes_update = notes.notes_update
    notes_delete = notes.notes_delete


async def init_controller(db: Any) -> Controller:

    if not isinstance(db, database.Database):
        raise Exception("invalid database instance")

    controller = Controller(db)

    return controller
