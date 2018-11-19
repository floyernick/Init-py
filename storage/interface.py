import abc

import models


class Storage(abc.ABC):
    @abc.abstractmethod
    async def get_note(self, id: str) -> models.Note:
        pass

    @abc.abstractmethod
    async def store_note(self, note: models.Note) -> None:
        pass

    @abc.abstractmethod
    async def update_note(self, note: models.Note) -> None:
        pass

    @abc.abstractmethod
    async def delete_note(self, id: str) -> None:
        pass
