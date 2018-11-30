from typing import Any
import json

import app
from . import utils


async def notes_get(self, r: Any):

    try:
        request_data = await r.json()
    except json.decoder.JSONDecodeError:
        return utils.error_response("invalid request data")

    try:
        response_data = await self.controller.notes_get(request_data)
    except app.DomainException as e:
        return utils.error_response(str(e))

    return utils.success_response(response_data)


async def notes_create(self, r: Any):

    try:
        request_data = await r.json()
    except json.decoder.JSONDecodeError:
        return utils.error_response("invalid request data")

    try:
        response_data = await self.controller.notes_create(request_data)
    except app.DomainException as e:
        return utils.error_response(str(e))

    return utils.success_response(response_data)


async def notes_update(self, r: Any):

    try:
        request_data = await r.json()
    except json.decoder.JSONDecodeError:
        return utils.error_response("invalid request data")

    try:
        response_data = await self.controller.notes_update(request_data)
    except app.DomainException as e:
        return utils.error_response(str(e))

    return utils.success_response(response_data)


async def notes_delete(self, r: Any):

    try:
        request_data = await r.json()
    except json.decoder.JSONDecodeError:
        return utils.error_response("invalid request data")

    try:
        response_data = await self.controller.notes_delete(request_data)
    except app.DomainException as e:
        return utils.error_response(str(e))

    return utils.success_response(response_data)
