from aiohttp import web

import usecases
from . import notes


class API:
    def __init__(self, controller: usecases.Controller):
        self.controller = controller

    notes_get = notes.notes_get
    notes_create = notes.notes_create
    notes_update = notes.notes_update
    notes_delete = notes.notes_delete


async def init_api(controller: usecases.Controller):

    api = API(controller)

    app = web.Application()

    app.add_routes([web.post("/notes.get", api.notes_get)])
    app.add_routes([web.post("/notes.create", api.notes_create)])
    app.add_routes([web.post("/notes.update", api.notes_update)])
    app.add_routes([web.post("/notes.delete", api.notes_delete)])

    return app
