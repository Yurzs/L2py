from abc import abstractmethod
from dataclasses import dataclass

from src.common.common.ctype import ctype
from src.common.common.dataclass import BaseDataclass


@dataclass(kw_only=True)
class Packet(BaseDataclass):
    type: ctype.int8

    @abstractmethod
    def encode(self):
        return self.body

    @property
    def body(self):
        data = bytearray()
        for field_name, field in self._fields.items():
            value = getattr(self, field_name)
            if isinstance(value, str):
                data.extend(bytearray(value, "utf-8"))
            elif isinstance(value, bytearray):
                data.extend(value)
            elif isinstance(value, bytes):
                data.extend(value)
            else:
                data.extend(value)
        return data

    @classmethod
    @abstractmethod
    def parse(cls, data, client):
        pass

    @classmethod
    @abstractmethod
    def decode(cls, data, client, **kwargs):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"
