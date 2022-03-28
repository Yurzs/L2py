import dataclasses
from abc import abstractmethod

import cython

import common.helpers.cython
from common.dataclass import BaseDataclass


@dataclasses.dataclass
class Packet(BaseDataclass):
    type: cython.char

    @abstractmethod
    def encode(self):
        return self.body

    @property
    def body(self):
        data = bytearray()
        for field_name, field in self._fields.items():
            value = getattr(self, field_name)
            field_type = field.type
            print(field_name, field_type, value)
            if isinstance(value, str):
                data.extend(bytearray(value, "utf-8"))
            elif isinstance(value, bytes):
                print(f"len: {len(value)}")
                data.extend(bytearray(value))
            else:
                print(f"len: {common.helpers.cython.get_len(field_type)}")
                data.extend(
                    bytearray(common.helpers.cython.convert_numeric_to_bytes(field_type, value))
                )
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
