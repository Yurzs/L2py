# This file is used for loading env and data types on app startup.
import pathlib
import sys

for module in ["common", "game", "login"]:
    sys.path.append(str(pathlib.Path(module).resolve()))
