import struct
from abc import ABCMeta


class DataType(metaclass=ABCMeta):
    struct_format: str
    prefix = "!"

    def __init__(self, data):
        if isinstance(data, DataType):
            self.value = data.value
        else:
            self.value = data

    def encode(self):
        from common.helpers.bytearray import to_bytearray

        return to_bytearray(struct.pack(f"{self.prefix}{self.struct_format}", self.value))

    @classmethod
    def decode(cls, data):
        return cls(struct.unpack(f"!{cls.struct_format}", data)[0])

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other

    def __hash__(self):
        return hash(self.value)
