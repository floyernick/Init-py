import tools.uuid as uuid


class Note:
    def __init__(self, id_: str = uuid.NIL_UUID, title: str = "", data: str = ""):
        self.__id = id_
        self.__title = title
        self.__data = data

    def exists(self) -> bool:
        return self.__id != uuid.NIL_UUID

    def get_id(self) -> str:
        return self.__id

    def set_id(self, value: str) -> None:
        self.__id = value

    def get_title(self) -> str:
        return self.__title

    def set_title(self, value: str) -> None:
        self.__title = value

    def get_data(self) -> str:
        return self.__data

    def set_data(self, value: str) -> None:
        self.__data = value
