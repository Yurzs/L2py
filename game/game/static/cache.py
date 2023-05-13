import json
from collections import defaultdict
from typing import ClassVar

from common.json import JsonDecoder
from common.misc import Singleton
from common.model import BaseModel


class StaticDataCache(BaseModel):
    data: ClassVar[defaultdict] = defaultdict(list)
    _instance = None

    def read(self, filepath, static_model):
        if filepath not in self.data:
            with open(filepath) as file:
                for item in json.loads(file.read(), cls=JsonDecoder):
                    self.data[filepath].append(static_model(**item))
        return self.data[filepath]
