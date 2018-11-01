from typing import Dict

from aiohttp import web


def success_response(result: Dict):
    response = {"status": True, "result": result}

    return web.json_response(data=response)


def error_response(error: str):
    response = {"status": False, "error": error}

    return web.json_response(data=response)
