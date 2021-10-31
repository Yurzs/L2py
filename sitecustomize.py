# This file is used for loading env and data types on app startup.
import pathlib
import sys

from dotenv import load_dotenv

for module in ["common", "data", "game", "login"]:
    sys.path.append(str(pathlib.Path(module).resolve()))

import common.datatypes  # noqa

load_dotenv()
