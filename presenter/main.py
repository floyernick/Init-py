from typing import Dict

from aiohttp import web

import controller
from . import notes


class Presenter:
    def __init__(self, controller_: controller.Controller):
        self.controller = controller_

    notes_get = notes.notes_get
    notes_create = notes.notes_create
    notes_update = notes.notes_update
    notes_delete = notes.notes_delete


async def init(config: Dict, controller_: controller.Controller):

    presenter = Presenter(controller_)

    app = web.Application()

    app.add_routes([
        web.post("/notes.get", presenter.notes_get),
        web.post("/notes.create", presenter.notes_create),
        web.post("/notes.update", presenter.notes_update),
        web.post("/notes.delete", presenter.notes_delete)
    ])

    runner = web.AppRunner(app, access_log=False)
    await runner.setup()
    site = web.TCPSite(
        runner,
        config["host"],
        config["port"],
        backlog=config["backlog"],
        reuse_port=True)
    await site.start()
