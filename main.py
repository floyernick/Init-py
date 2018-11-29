import sys
import logging

import config
import storage
import presenter
import controller


async def init() -> None:

    try:
        config_ = await config.load_config()
    except Exception as e:
        logging.error(e)
        sys.exit(1)

    try:
        storage_ = await storage.init(config_["db"])
    except Exception as e:
        logging.error(e)
        sys.exit(1)

    try:
        controller_ = await controller.init(storage_)
    except Exception as e:
        logging.error(e)
        sys.exit(1)

    try:
        presenter_ = await presenter.init(controller_)
    except Exception as e:
        logging.error(e)
        sys.exit(1)

    return presenter_
