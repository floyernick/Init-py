from __future__ import annotations
import abc

import models


class Storage(abc.ABC):
    @abc.abstractmethod
    async def commit(self) -> None:
        pass

    @abc.abstractmethod
    async def rollback(self) -> None:
        pass

    @abc.abstractmethod
    async def transaction(self) -> Storage:
        pass

    @abc.abstractmethod
    async def get_note(self, id_: str) -> models.Note:
        pass

    @abc.abstractmethod
    async def store_note(self, note: models.Note) -> None:
        pass

    @abc.abstractmethod
    async def update_note(self, note: models.Note) -> None:
        pass

    @abc.abstractmethod
    async def delete_note(self, note: models.Note) -> None:
        pass
