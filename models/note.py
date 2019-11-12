import tools.uuid as uuid


class Note:
    def __init__(self, id_: str = uuid.NIL_UUID, title: str = "", data: str = ""):
        self.id: str = id_
        self.title: str = title
        self.data: str = data

    def exists(self) -> bool:
        return self.id != uuid.NIL_UUID
