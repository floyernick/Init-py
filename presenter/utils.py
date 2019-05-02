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


async def respond_with_success(result: Dict[str, Any]):
    response_body = {"status": True, "result": result}
    return await respond(response_body)


async def respond_with_error(error: str):
    response_body = {"status": False, "error": error}
    return await respond(response_body)


async def respond(response_body: Dict[str, Any]):
    return web.Response(text=json.dumps(response_body), content_type="application/json")
