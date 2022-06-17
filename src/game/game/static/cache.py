import dataclasses
import json
from collections import defaultdict

from src.common.common.dataclass import BaseDataclass
from src.common.common.json import JsonDecoder
from src.common.common.misc import Singleton


class StaticDataCache(BaseDataclass, metaclass=Singleton):
    data = defaultdict(list)

    def read(self, filepath, static_model):
        if filepath not in self.data:
            with open(filepath) as file:
                for item in json.loads(file.read(), cls=JsonDecoder):
                    self.data[filepath].append(static_model(**item))
        return self.data[filepath]
