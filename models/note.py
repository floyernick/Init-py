from dataclasses import dataclass

import tools.uuid as uuid


@dataclass
class Note:
    id: str = uuid.NIL_UUID
    title: str = ""
    data: str = ""
