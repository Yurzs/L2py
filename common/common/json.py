import json
from typing import Any

import bson

from common.ctype import _Numeric, extras
from common.model import BaseModel


class JsonEncoder(json.JSONEncoder):
    def encode(self, o: Any):
        if isinstance(o, BaseModel):
            return {**o.dict(), "$model": o.__class__.__name__}
        elif isinstance(o, (bytes, str)):
            return str(o)
        elif isinstance(o, int):
            return int(o)
        elif isinstance(o, bson.ObjectId):
            return {"$oid": str(o)}
        elif isinstance(o, list):
            return [self.encode(item) for item in o]
        elif isinstance(o, _Numeric):
            value = o.value
            if isinstance(o.value, bytes):
                value = int.from_bytes(o.value, "big")
            return extras[o.__class__][0](value)
        if isinstance(o, dict):
            return o
        if o is None:
            return None
        return super().default(o)

    def encode_dict(self, o: dict):
        """Encodes all values in dict."""

        encoded = {}
        for key, value in o.items():
            if isinstance(value, dict):
                encoded[key] = self.encode_dict(value)
            else:
                encoded[key] = self.encode(value)

        return encoded


class JsonDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, data):
        if isinstance(data, dict):
            if "$oid" in data:
                return bson.ObjectId(data["$oid"])
            elif "$model" in data:
                for model in BaseModel.__subclasses__():
                    if model.__name__ == data["$model"]:
                        return model(**data)
        return data
