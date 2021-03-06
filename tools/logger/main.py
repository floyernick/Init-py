from typing import Union
import inspect
import datetime

DEBUG_LEVEL = 35
INFO_LEVEL = 36
WARNING_LEVEL = 33
ERROR_LEVEL = 31


async def log(level: int, message: Union[Exception, str]) -> None:
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file = inspect.stack()[2][1]
    function = inspect.stack()[2][3]
    print(f"\033[{level}m●\033[0m {time} | {file}::{function} | {message}")


async def debug(message: Union[Exception, str]) -> None:
    await log(DEBUG_LEVEL, message)


async def info(message: Union[Exception, str]) -> None:
    await log(INFO_LEVEL, message)


async def warning(message: Union[Exception, str]) -> None:
    await log(WARNING_LEVEL, message)


async def error(message: Union[Exception, str]) -> None:
    await log(ERROR_LEVEL, message)
