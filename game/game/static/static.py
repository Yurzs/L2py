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
        return StaticDataCache().read(cls.__filepath__, cls)
