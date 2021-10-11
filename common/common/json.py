import json
from typing import Any

import bson

from common.dataclass import _DATACLASS_MAP, BaseDataclass
from common.datatypes import Int


class JsonEncoder(json.JSONEncoder):
    def default(self, o: Any):
        if isinstance(o, BaseDataclass):
            result = o.to_dict()
            result["$model"] = o.__class__.__name__.lower()
            return result
        elif isinstance(o, Int):
            return int(o)
        elif isinstance(o, bson.ObjectId):
            return {"$oid": str(o)}
        return super().default(o)


class JsonDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, data):
        from data.models.account import Account  # noqa: F401
        from data.models.game_server import GameServer  # noqa: F401
        from data.models.login_server import LoginServer  # noqa: F401

        if isinstance(data, dict):
            if "$model" in data:
                return _DATACLASS_MAP[data.pop("$model")](**data)
            elif "$oid" in data:
                return bson.ObjectId(data["$oid"])
        return data
