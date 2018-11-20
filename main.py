import config
import storage
import presenter
import controller


async def init() -> None:

    cfg = await config.load_config()

    db = await storage.init(cfg["db"])

    ctrl = await controller.init(db)

    api = await presenter.init(ctrl)

    return api
