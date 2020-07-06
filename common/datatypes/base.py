import struct
from abc import ABCMeta


class DataType(metaclass=ABCMeta):
    struct_format: str

    def __init__(self, python_data):
        if isinstance(python_data, DataType):
            self.value = python_data.value
        else:
            self.value = python_data

    def encode(self):
        from common.helpers.bytearray import to_bytearray
        return to_bytearray(struct.pack(f"!{self.struct_format}", self.value))

    @classmethod
    def decode(cls, data):
        return cls(struct.unpack(f"!{cls.struct_format}", data)[0])

    def __repr__(self):
        return str(self.value)
