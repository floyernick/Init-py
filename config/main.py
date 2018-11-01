import os
from typing import Dict

import yaml

location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

name = "default"


async def load_config() -> Dict:
    f = open(os.path.join(location, "{}.yaml".format(name)), "r")
    d = yaml.load(f)
    return d
