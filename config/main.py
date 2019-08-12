import os
from typing import Dict, Any


async def init() -> Dict[str, Any]:

    config = {
        "server": {
            "host": os.environ["INIT_SERVER_HOST"],
            "port": int(os.environ["INIT_SERVER_PORT"]),
            "backlog": int(os.environ["INIT_SERVER_BACKLOG"])
        },
        "db": {
            "url": os.environ["INIT_DB_URL"],
            "min_conns": int(os.environ["INIT_DB_MIN_CONNS"]),
            "max_conns": int(os.environ["INIT_DB_MAX_CONNS"]),
            "conn_lifetime": int(os.environ["INIT_DB_CONN_LIFETIME"]),
            "conn_timeout": int(os.environ["INIT_DB_CONN_TIMEOUT"])
        }
    }

    return config
