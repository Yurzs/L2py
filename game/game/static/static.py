import json
import os
import pathlib
import typing

from common.dataclass import BaseDataclass

from .cache import StaticDataCache


class StaticData(BaseDataclass):
    __filepath__: str

    @classmethod
    def read_file(cls) -> typing.List["StaticData"]:
        result = []
        cache = StaticDataCache()
        print(pathlib.Path(os.curdir).resolve())
        for item in json.loads(cache.read(cls.__filepath__)):
            result.append(cls(**item))
        return result
