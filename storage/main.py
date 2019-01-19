from typing import Dict, Union

import asyncpg

import app
import tools.logger as logger
from . import interface
from . import notes


async def transaction(self) -> 'Storage':
    try:
        conn = await self.pool.acquire()
        tx = conn.transaction()
        await tx.start()
    except Exception as e:
        await logger.warning(e)
        raise app.StorageException
    return Storage(self.pool, conn, tx)


async def commit(self) -> None:
    try:
        await self.tx.commit()
        await self.pool.release(self.conn)
    except Exception as e:
        await logger.warning(e)
        raise app.StorageException


async def rollback(self) -> None:
    try:
        await self.tx.rollback()
        await self.pool.release(self.conn)
    except Exception as e:
        await logger.warning(e)


def performer(self) -> Union[asyncpg.pool.Pool, asyncpg.connection.Connection]:
    if self.tx is not None:
        return self.conn
    else:
        return self.pool


class Storage(interface.Storage):
    def __init__(self,
                 pool: asyncpg.pool.Pool,
                 conn: asyncpg.connection.Connection = None,
                 tx: asyncpg.transaction.Transaction = None):
        self.pool = pool
        self.conn = conn
        self.tx = tx

    transaction = transaction
    commit = commit
    rollback = rollback

    performer = performer

    get_note = notes.get_note
    store_note = notes.store_note
    update_note = notes.update_note
    delete_note = notes.delete_note


async def init(cfg: Dict) -> Storage:

    pool = await asyncpg.create_pool(
        dsn=cfg["url"],
        min_size=cfg["min_conns"],
        max_size=cfg["max_conns"],
        timeout=cfg["conn_timeout"],
        max_inactive_connection_lifetime=cfg["conn_lifetime"])

    db = Storage(pool)

    return db
