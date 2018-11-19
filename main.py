import config
import storage
import presenter
import usecases


async def init() -> None:

    cfg = await config.load_config()

    db = await storage.init(cfg["db"])

    controller = await usecases.init_controller(db)

    api = await presenter.init(controller)

    return api
