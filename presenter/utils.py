from typing import Dict, Any
import json

from aiohttp import web

import app.errors as errors


@web.middleware
async def handle(request, handler):
    try:
        result = await handler(request)
    except (errors.DomainException, errors.PresenterException) as e:
        return await respond_with_error(e.description)
    return await respond_with_success(result)


async def parse_request_body(request: Any) -> Dict:
    try:
        request_body = await request.json()
    except json.decoder.JSONDecodeError:
        raise errors.InvalidRequest
    return request_body


async def respond_with_success(result: Dict):
    return await respond(200, result)


async def respond_with_error(error: str):
    result = {"error": error}
    return await respond(400, result)


async def respond(status: int, result: Dict[str, Any]):
    response = web.Response(status=status, content_type="application/json", text=json.dumps(result))
    return response
