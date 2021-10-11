import json
import typing

from common.dataclass import BaseDataclass


class StaticData(BaseDataclass):
    __filepath__: str

    @classmethod
    def read_file(cls) -> typing.List["StaticData"]:
        result = []
        with open(cls.__filepath__) as static_file:
            for item in json.loads(static_file.read()):
                result.append(cls(**item))
        return result
