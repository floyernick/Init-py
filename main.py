import sys
import asyncio

import uvloop

import config
import storage
import presenter
import controller
import tools.logger as logger

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def init() -> None:

    try:
        config_ = await config.load_config()
    except Exception as e:
        await logger.error("failed to load config: {}".format(str(e)))
        sys.exit(1)

    try:
        storage_ = await storage.init(config_["db"])
    except Exception as e:
        await logger.error("failed to init storage: {}".format(str(e)))
        sys.exit(1)

    try:
        controller_ = await controller.init(storage_)
    except Exception as e:
        await logger.error("failed to init controller: {}".format(str(e)))
        sys.exit(1)

    try:
        await presenter.init(config_["server"], controller_)
    except Exception as e:
        await logger.error("failed to init presenter: {}".format(str(e)))
        sys.exit(1)


loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()
