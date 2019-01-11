import tools.uuid as uuid


class Note:
    def __init__(self,
                 id_: str = uuid.NIL_UUID,
                 title: str = "",
                 data: str = ""):
        self.id = id_
        self.title = title
        self.data = data
