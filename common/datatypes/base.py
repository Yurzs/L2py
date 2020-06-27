import struct
from abc import ABCMeta


class DataType(metaclass=ABCMeta):
    struct_format: str

    def __init__(self, python_data):
        if isinstance(python_data, DataType):
            self.data = python_data.data
        else:
            self.data = python_data

    def encode(self):
        return struct.pack(f"!{self.struct_format}", self.data)

    @classmethod
    def decode(cls, data):
        return cls(struct.unpack(f"!{cls.struct_format}", data)[0])

    def __repr__(self):
        return str(self.data)
