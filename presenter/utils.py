from typing import Dict, Any, Callable, Optional
import json

from aiohttp import web

import app.errors as errors


@web.middleware
async def handle(request: Any, handler: Callable):
    if request.method == "OPTIONS":
        return await respond(200)
    try:
        response = await handler(request)
    except (errors.DomainException, errors.PresenterException) as e:
        return await respond_with_error(e.description)
    return await respond_with_success(response)


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


async def respond(status: int, result: Optional[Dict[str, Any]] = None):
    response = web.Response(
        status=status,
        content_type="application/json",
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Authorization",
        },
    )
    if result is not None:
        response.text = json.dumps(result)
    return response
