import random

import cython

CYTHON_TYPES_LEN = {
    cython.bint: 1,
    cython.char: 1,
    cython.uchar: 1,
    cython.int: 4,
    cython.uint: 4,
    cython.long: 8,
    cython.ulong: 8,
    cython.longlong: 16,
    cython.ulonglong: 16,
    cython.bint.name: 1,
    cython.char.name: 1,
    cython.uchar.name: 1,
    cython.int.name: 4,
    cython.uint.name: 4,
    cython.long.name: 8,
    cython.ulong.name: 8,
    cython.longlong.name: 16,
    cython.ulonglong.name: 16,
}

UNSIGNED_TYPES = [cython.uchar, cython.uint, cython.ulong, cython.ulonglong]


def get_len(cython_type):
    return CYTHON_TYPES_LEN[cython_type.name]


def get_random(cython_type):
    return random.randrange(2 ** cython_type)


def convert_numeric_to_bytes(cython_type, value: cython.int_types) -> bytearray:
    length = get_len(cython_type)
    return bytearray(value.to_bytes(length, "little", signed=cython_type not in UNSIGNED_TYPES))


def convert_numeric_from_bytes(cython_type, data: bytearray):
    length = get_len(cython_type)
    return int.from_bytes(data[:length], "little", signed=cython_type not in UNSIGNED_TYPES)


class utf8str(str):
    @classmethod
    def decode(cls, data: bytearray):
        return cls(data.rstrip(b"\x00").decode("utf-8"))

    def encode(self) -> bytes:
        return super().encode("utf-8")


class utf16str(str):
    @classmethod
    def decode(cls, data: bytearray):
        return cls(data.rstrip(b"\x00\x00").decode("utf-16-le"))

    def encode(self) -> bytes:
        return super().encode("utf-16-le")
