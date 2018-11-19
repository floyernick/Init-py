from typing import Dict

import asyncpg

from . import interface
from . import notes


class StorageImpl(interface.Storage):
    def __init__(self, pool: asyncpg.pool.Pool):
        self.pool = pool

    get_note = notes.get_note
    store_note = notes.store_note
    update_note = notes.update_note
    delete_note = notes.delete_note


async def init(cfg: Dict) -> StorageImpl:

    pool = await asyncpg.create_pool(
        dsn=cfg["url"],
        min_size=cfg["min_conns"],
        max_size=cfg["max_conns"],
        timeout=cfg["conn_timeout"],
        max_inactive_connection_lifetime=cfg["conn_lifetime"])

    db = StorageImpl(pool)

    return db
