import os
from typing import Dict, Any

import yaml

file_location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file_name = "default"


async def load_config() -> Dict[str, Any]:
    file = open(os.path.join(file_location, "{}.yaml".format(file_name)), "r")
    config = yaml.load(file)
    return config
