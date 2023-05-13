from pathlib import Path
from typing import ClassVar

from common.model import BaseModel

from .cache import StaticDataCache


class StaticData(BaseModel):
    filepath: ClassVar[str]

    @classmethod
    def read_file(cls) -> list["StaticData"]:
        import game

        game_root = Path(game.__path__[0]).parent
        return StaticDataCache().read(Path(game_root, cls.filepath), cls)
