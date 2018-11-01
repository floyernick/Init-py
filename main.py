import config
import database.postgres
import transfer.api
import usecases


async def init() -> None:

    cfg = await config.load_config()

    db = await database.postgres.init_db(cfg["db"])

    controller = await usecases.init_controller(db)

    api = await transfer.api.init_api(controller)

    return api
