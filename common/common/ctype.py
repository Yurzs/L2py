import ctypes
import random
import struct

from common.misc import classproperty


class _Numeric:
    _type_: str

    def __init__(self, value):
        if isinstance(value, (bytearray, bytes)):
            value = struct.unpack(self._type_, value)[0]
        if isinstance(value, _Numeric):
            value = value.value
        if "int" in self.__class__.__name__:
            value = int(value)
        super().__init__(value)

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, args, kwargs)

    def __and__(self, other: int):
        if isinstance(other, _Numeric):
            return self.__class__(self.value & other.value)
        return self.__class__(self.value & other)

    def __lshift__(self, other):
        if isinstance(other, _Numeric):
            return self.__class__(self.value << other.value)
        return self.__class__(self.value << other)

    def __rshift__(self, other):
        if isinstance(other, _Numeric):
            return self.__class__(self.value >> other.value)
        return self.__class__(self.value >> other)

    def __xor__(self, other):
        if isinstance(other, _Numeric):
            return self.__class__(self.value ^ other.value)
        # if isinstance(self.value, bytes):
        #     return self.__class__(int.from_bytes(self.value, 1) ^ other)
        return self.__class__(self.value ^ other)

    def __ixor__(self, other):
        self.value = (self ^ other).value
        return self

    def __or__(self, other):
        if isinstance(other, _Numeric):
            return self.__class__(self.value | other.value)
        return self.__class__(self.value | other)

    def __ior__(self, other):
        self.value = (self | other).value
        return self

    def __add__(self, other):
        if isinstance(other, _Numeric):
            return self.__class__(self.value + other.value)
        return self.__class__(self.value + other)

    def __iadd__(self, other):
        other_value = other
        if isinstance(other, _Numeric):
            other_value = other.value
        self.value = self.value + other_value
        return self

    def __radd__(self, other):
        return self + other

    def __repr__(self):
        return str(self.value)

    def __bytes__(self):
        return bytes(bytearray(self))

    def __sub__(self, other):
        if isinstance(other, _Numeric):
            return self.__class__(self.value - other.value)
        return self.__class__(self.value - other)

    def __isub__(self, other):
        self.value = (self - other).value
        return self

    def __lt__(self, other):
        if isinstance(other, _Numeric):
            return self.value < other.value
        else:
            return self.value < other

    def __gt__(self, other):
        if isinstance(other, _Numeric):
            return self.value > other.value
        else:
            return self.value > other

    def __ge__(self, other):
        if isinstance(other, _Numeric):
            return self.value >= other.value
        return self.value >= other

    def __int__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, _Numeric):
            return self.value == other.value
        else:
            return self.value == other

    def __len__(self):
        return ctypes.sizeof(self)

    def __reversed__(self):
        return self.__class__(self.encode().data[::-1])

    @classproperty
    def __extra__(cls):
        return (cls, *extras[cls])

    @classmethod
    def random(cls):
        return cls(random.randrange(0, 2 ** (ctypes.sizeof(cls) * 8)))

    def __hash__(self):
        return hash(self.value)

    def __truediv__(self, other):
        other_value = other
        if isinstance(other, _Numeric):
            other_value = other.value
        return ctype.float(self.value / other_value)

    def __floordiv__(self, other):
        other_value = other
        if isinstance(other, _Numeric):
            other_value = other.value
        return self.__class__(self.value // other_value)

    def __mul__(self, other):
        other_value = other
        if isinstance(other, _Numeric):
            other_value = other.value
        return self.__class__(self.value * other_value)


def _make_ctype_from_ctypes(ctypes_type):
    ctypes_namespace = dict(ctypes_type.__dict__)

    namespace = {
        "__module__": _Numeric.__module__,
        "_type_": ctypes_namespace["_type_"],
    }

    return type(
        ctypes_type.__name__.replace("c_", ""),
        tuple([_Numeric, *ctypes.c_bool.__bases__]),
        namespace,
    )


class ctype:  # noqa
    bool = _make_ctype_from_ctypes(ctypes.c_bool)
    byte = _make_ctype_from_ctypes(ctypes.c_byte)
    char = _make_ctype_from_ctypes(ctypes.c_char)
    short = _make_ctype_from_ctypes(ctypes.c_short)
    ushort = _make_ctype_from_ctypes(ctypes.c_ushort)
    int = _make_ctype_from_ctypes(ctypes.c_int)
    uint = _make_ctype_from_ctypes(ctypes.c_uint)
    long = _make_ctype_from_ctypes(ctypes.c_long)
    ulong = _make_ctype_from_ctypes(ctypes.c_ulong)
    longlong = _make_ctype_from_ctypes(ctypes.c_longlong)
    ulonglong = _make_ctype_from_ctypes(ctypes.c_ulonglong)
    double = _make_ctype_from_ctypes(ctypes.c_double)
    float = _make_ctype_from_ctypes(ctypes.c_float)
    int8 = _make_ctype_from_ctypes(ctypes.c_int8)
    uint8 = _make_ctype_from_ctypes(ctypes.c_uint8)
    int16 = _make_ctype_from_ctypes(ctypes.c_int16)
    uint16 = _make_ctype_from_ctypes(ctypes.c_uint16)
    int32 = _make_ctype_from_ctypes(ctypes.c_int32)
    uint32 = _make_ctype_from_ctypes(ctypes.c_uint32)
    int64 = _make_ctype_from_ctypes(ctypes.c_int64)
    uint64 = _make_ctype_from_ctypes(ctypes.c_uint64)


extras = {
    ctype.bool: (bool,),
    ctype.byte: (int,),
    ctype.char: (int,),
    ctype.short: (int,),
    ctype.ushort: (int,),
    ctype.int: (int,),
    ctype.uint: (int,),
    ctype.long: (int,),
    ctype.ulong: (int,),
    ctype.longlong: (int,),
    ctype.ulonglong: (int,),
    ctype.double: (float, int),
    ctype.float: (float, int),
    ctype.int8: (int,),
    ctype.int16: (int,),
    ctype.int32: (int,),
    ctype.int64: (int,),
    ctype.uint8: (int,),
    ctype.uint16: (int,),
    ctype.uint32: (int,),
    ctype.uint64: (int,),
}
