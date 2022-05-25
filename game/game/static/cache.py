import dataclasses
import json
from collections import defaultdict

from common.dataclass import BaseDataclass
from common.json import JsonDecoder
from common.misc import Singleton


class StaticDataCache(BaseDataclass, metaclass=Singleton):
    data = defaultdict(list)

    def read(self, filepath, static_model):
        if filepath not in self.data:
            with open(filepath) as file:
                for item in json.loads(file.read(), cls=JsonDecoder):
                    self.data[filepath].append(static_model(**item))
        return self.data[filepath]
