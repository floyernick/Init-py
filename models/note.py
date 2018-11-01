import tools.uuid

class Note:
    def __init__(self, id: str = tools.uuid.NIL_UUID, title: str = "", data: str = ""):
        self.id = id
        self.title = title
        self.data = data
