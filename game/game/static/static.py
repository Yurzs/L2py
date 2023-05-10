from typing import ClassVar

from common.model import BaseModel

from .cache import StaticDataCache


class StaticData(BaseModel):
    filepath: ClassVar[str]

    @classmethod
    def read_file(cls) -> list["StaticData"]:
        return StaticDataCache().read(cls.filepath, cls)
