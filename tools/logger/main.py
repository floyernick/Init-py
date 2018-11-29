import inspect
import datetime
import logging

logging.basicConfig(
    format='%(level)s %(time)s | %(caller)s | %(message)s', level=logging.INFO)

DEBUG_LEVEL = 35
INFO_LEVEL = 36
WARNING_LEVEL = 33
ERROR_LEVEL = 31


async def log(level: int, message: str) -> None:
    logging.info(
        message,
        extra={
            "level": "\033[%dm●\033[0m" % level,
            "caller":
            "%s::%s" % (inspect.stack()[2][1], inspect.stack()[2][3]),
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })


async def debug(message: str) -> None:
    await log(DEBUG_LEVEL, message)


async def info(message: str) -> None:
    await log(INFO_LEVEL, message)


async def warning(message: str) -> None:
    await log(WARNING_LEVEL, message)


async def error(message: str) -> None:
    await log(ERROR_LEVEL, message)
