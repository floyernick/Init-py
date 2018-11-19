import config
import storage
import transfer.api
import usecases


async def init() -> None:

    cfg = await config.load_config()

    db = await storage.init(cfg["db"])

    controller = await usecases.init_controller(db)

    api = await transfer.api.init_api(controller)

    return api
