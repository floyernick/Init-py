from __future__ import annotations
from typing import Any, Dict

from . import utils

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .main import Presenter


async def notes_get(self: Presenter, request: Any) -> Dict[str, Any]:
    request_body = await utils.parse_request_body(request)
    result = await self.controller.notes_get(request_body)
    return result


async def notes_list(self: Presenter, request: Any) -> Dict[str, Any]:
    request_body = await utils.parse_request_body(request)
    result = await self.controller.notes_list(request_body)
    return result


async def notes_create(self: Presenter, request: Any) -> Dict[str, Any]:
    request_body = await utils.parse_request_body(request)
    result = await self.controller.notes_create(request_body)
    return result


async def notes_update(self: Presenter, request: Any) -> Dict[str, Any]:
    request_body = await utils.parse_request_body(request)
    result = await self.controller.notes_update(request_body)
    return result


async def notes_delete(self: Presenter, request: Any) -> Dict[str, Any]:
    request_body = await utils.parse_request_body(request)
    result = await self.controller.notes_delete(request_body)
    return result
