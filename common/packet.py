import dataclasses
from abc import abstractmethod

from common.dataclass import BaseDataclass
from common.datatypes import Int8
from common.helpers.bytearray import ByteArray


@dataclasses.dataclass
class Packet(BaseDataclass):
    type: Int8

    @abstractmethod
    def encode(self):
        return self.body

    @property
    def body(self):
        data = ByteArray(b"")
        for arg in self.__class__.__dataclass_fields__.keys():
            data.extend(getattr(self, arg).encode())
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
