class PresenterException(Exception):
    description = ""


class InvalidRequest(PresenterException):
    description = "invalid request"


class DomainException(Exception):
    description = ""


class InvalidParams(DomainException):
    description = "invalid params"


class InternalError(DomainException):
    description = "internal error"


class NoteNotFound(DomainException):
    description = "note not found"


class StorageException(Exception):
    description = ""
