from __future__ import annotations
from typing import Dict, Union, Any, Optional

import asyncpg

import app.errors as errors
import tools.logger as logger
from . import interface
from . import notes


async def transaction(self: Storage) -> Storage:
    try:
        conn = await self.pool.acquire()
        tx = conn.transaction()
        await tx.start()
    except Exception as e:
        await logger.warning(e)
        raise errors.StorageException
    return Storage(self.pool, conn, tx)


async def commit(self: Storage) -> None:
    if self.tx is None:
        return
    try:
        await self.tx.commit()
        await self.pool.release(self.conn)
    except Exception as e:
        await logger.warning(e)
        raise errors.StorageException


async def rollback(self: Storage) -> None:
    if self.tx is None:
        return
    try:
        await self.tx.rollback()
        await self.pool.release(self.conn)
    except Exception as e:
        await logger.warning(e)


class Storage(interface.Storage):
    def __init__(
        self,
        pool: asyncpg.pool.Pool,
        conn: Optional[asyncpg.connection.Connection] = None,
        tx: Optional[asyncpg.transaction.Transaction] = None,
    ):
        self.pool = pool
        self.conn = conn
        self.tx = tx

    def performer(self) -> Union[asyncpg.pool.Pool, asyncpg.connection.Connection]:
        if self.tx is not None:
            return self.conn
        else:
            return self.pool

    transaction = transaction
    commit = commit
    rollback = rollback

    get_notes = notes.get_notes
    store_note = notes.store_note
    update_note = notes.update_note
    delete_note = notes.delete_note


async def init(config: Dict[str, Any]) -> Storage:

    pool = await asyncpg.create_pool(
        dsn=config["url"],
        min_size=config["min_conns"],
        max_size=config["max_conns"],
        timeout=config["conn_timeout"],
        max_inactive_connection_lifetime=config["conn_lifetime"],
    )

    storage = Storage(pool)

    return storage
