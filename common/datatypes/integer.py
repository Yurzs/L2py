import ctypes
import struct

from .base import DataType


class Int:
    ctype = ctypes.c_int
    signed = True
    length = 4

    def __init__(self, value):
        from common.helpers.bytearray import ByteArray

        if isinstance(value, Int):
            super(self.ctype, self).__init__(value.value)
        elif isinstance(value, DataType):
            super(self.ctype, self).__init__(value.data)
        elif isinstance(value, list):
            super(self.ctype, self).__init__(int.from_bytes(bytes(ByteArray(value)), "big"))
        else:
            super(self.ctype, self).__init__(int(value))

    def encode(self):
        from common.helpers.bytearray import ByteArray
        return ByteArray(self.value.to_bytes(self.length, "big", signed=self.signed))

    @classmethod
    def decode(cls, data):
        return cls(struct.unpack(f"<{cls.struct_format}", data)[0])

    @classmethod
    def new(cls, value):
        return cls(value)

    def __and__(self, other: int):
        if isinstance(other, Int):
            return self.new(self.value & other.value)
        return self.new(self.value & other)

    def __lshift__(self, other):
        if isinstance(other, Int):
            return self.new(self.value << other.value)
        return self.new(self.value << other)

    def __rshift__(self, other):
        if isinstance(other, Int):
            return self.new(self.value >> other.value)
        return self.new(self.value >> other)

    def __xor__(self, other):
        if isinstance(other, Int):
            return self.new(self.value ^ other.value)
        return self.new(self.value ^ other)

    def __ixor__(self, other):
        self.value = (self ^ other).value
        return self

    def __or__(self, other):
        if isinstance(other, Int):
            return self.new(self.value | other.value)
        return self.new(self.value | other)

    def __ior__(self, other):
        self.value = (self | other).value
        return self

    def __add__(self, other):
        if isinstance(other, Int):
            return self.new(self.value + other.value)
        return self.new(self.value + other)

    def __iadd__(self, other):
        self.value = (self.value + other).value
        return self

    def __radd__(self, other):
        return self + other

    def __repr__(self):
        return str(self.value)

    def __bytes__(self):
        value = ctypes.c_uint(self.value)
        return bytes(value.value)

    def __sub__(self, other):
        if isinstance(other, Int):
            return self.new(self.value - other.value)
        return self.new(self.value - other)

    def __isub__(self, other):
        self.value = (self - other).value
        return self

    def __lt__(self, other):
        if isinstance(other, Int):
            return self.value < other.value
        else:
            return self.value < other

    def __gt__(self, other):
        if isinstance(other, Int):
            return self.value > other.value
        else:
            return self.value > other

    def __int__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, Int):
            return self.value == other.value
        else:
            return self.value == other


class UInt(Int):
    length = 4
    ctype = ctypes.c_uint
    signed = False


class Int8(Int, ctypes.c_int8):
    length = 1
    ctype = ctypes.c_int8


class Int16(Int, ctypes.c_int16):
    length = 2
    ctype = ctypes.c_int16


class Int32(Int, ctypes.c_int32):
    length = 4
    ctype = ctypes.c_int32


class Int64(Int, ctypes.c_int64):
    length = 8
    ctype = ctypes.c_int64


class UInt8(UInt, ctypes.c_uint8):
    length = 1
    ctype = ctypes.c_uint8


class UInt16(UInt, ctypes.c_uint16):
    length = 2
    ctype = ctypes.c_uint16


class UInt32(UInt, ctypes.c_uint32):
    length = 4
    ctype = ctypes.c_uint32
