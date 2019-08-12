import uuid

NIL_UUID = "00000000-0000-0000-0000-000000000000"


def generate() -> str:
    return str(uuid.uuid4())
