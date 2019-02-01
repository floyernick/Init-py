class PresenterException(Exception):
    pass


class InvalidRequest(PresenterException):
    description = "invalid request"


class DomainException(Exception):
    pass


class InvalidParams(DomainException):
    description = "invalid params"


class InternalError(DomainException):
    description = "internal error"


class NoteNotFound(DomainException):
    description = "note not found"


class StorageException(Exception):
    pass
