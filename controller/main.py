import storage
from . import notes


class Controller:
    def __init__(self, storage_: storage.Storage):
        self.storage = storage_

    notes_get = notes.notes_get
    notes_create = notes.notes_create
    notes_update = notes.notes_update
    notes_delete = notes.notes_delete


async def init(storage_: storage.Storage) -> Controller:
    controller = Controller(storage_)
    return controller
