import ctypes
import random
import struct

from common.misc import classproperty


class _CType:
    @classmethod
    def validate(cls, value):
        try:
            cls(value)
        except ValueError:
            raise ValueError(f"Value {value} is not a valid {cls.__name__}")

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        pass


class _Bool(_CType):
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="boolean")


class _Char(_CType):
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="integer", minimum=0, maximum=255)


class _Integer(_CType):
    @classmethod
    def __limits__(cls) -> tuple[int, int]:
        is_signed = cls(-1) > cls(0)
        bit_size = ctypes.sizeof(cls) * 8
        signed_limit = 2 ** (bit_size - 1)
        return (-signed_limit, signed_limit - 1) if is_signed else (0, 2 * signed_limit - 1)

    @classmethod
    def __modify_schema__(cls, field_schema):
        limit_min, limit_max = cls.__limits__()
        field_schema.update(type="integer", minimum=limit_min, maximum=limit_max)


class _Float(_CType):
    @classmethod
    def __limits__(cls) -> tuple[int, int]:
        bit_size = ctypes.sizeof(cls) * 8
        signed_limit = 2 ** (bit_size - 1)
        return -signed_limit, signed_limit - 1

    @classmethod
    def __modify_schema__(cls, field_schema):
        limit_min, limit_max = cls.__limits__()
        field_schema.update(type="float", mininum=limit_min, maximum=limit_max)


class _Numeric:
    _type_: str

    def __init__(self, value):
        if isinstance(value, (bytearray, bytes)):
            value = struct.unpack(self._type_, value)[0]
        if isinstance(value, _Char):
            value = int.from_bytes(value.value, "big")
        elif isinstance(value, _Numeric):
            value = value.value
        if isinstance(self, _Integer):
            value = int(value)
        elif isinstance(self, _Float):
            value = float(value)
        elif isinstance(self, _Bool):
            value = bool(value)
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

    def __imod__(self, other):
        other_value = other
        if isinstance(other, _Numeric):
            other_value = other.value
        self.value = self.value % other_value
        return self

    def __mod__(self, other):
        other_value = other
        if isinstance(other, _Numeric):
            other_value = other.value
        return self.__class__(self.value % other_value)

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


def _make_ctype_from_ctypes(ctypes_type, *extra_bases):
    ctypes_namespace = dict(ctypes_type.__dict__)

    namespace = {
        "__module__": _Numeric.__module__,
        "_type_": ctypes_namespace["_type_"],
    }

    return type(
        ctypes_type.__name__.replace("c_", ""),
        tuple([_Numeric, *extra_bases, *ctypes_type.__bases__]),
        namespace,
    )


class ctype:  # noqa
    bool = _make_ctype_from_ctypes(ctypes.c_bool, _Bool)
    byte = _make_ctype_from_ctypes(ctypes.c_byte, _Integer)
    char = _make_ctype_from_ctypes(ctypes.c_char, _Char)
    short = _make_ctype_from_ctypes(ctypes.c_short, _Integer)
    ushort = _make_ctype_from_ctypes(ctypes.c_ushort, _Integer)
    int = _make_ctype_from_ctypes(ctypes.c_int, _Integer)
    uint = _make_ctype_from_ctypes(ctypes.c_uint, _Integer)
    long = _make_ctype_from_ctypes(ctypes.c_long, _Integer)
    ulong = _make_ctype_from_ctypes(ctypes.c_ulong, _Integer)
    longlong = _make_ctype_from_ctypes(ctypes.c_longlong, _Integer)
    ulonglong = _make_ctype_from_ctypes(ctypes.c_ulonglong, _Integer)
    double = _make_ctype_from_ctypes(ctypes.c_double, _Float)
    float = _make_ctype_from_ctypes(ctypes.c_float, _Float)
    int8 = _make_ctype_from_ctypes(ctypes.c_int8, _Integer)
    uint8 = _make_ctype_from_ctypes(ctypes.c_uint8, _Integer)
    int16 = _make_ctype_from_ctypes(ctypes.c_int16, _Integer)
    uint16 = _make_ctype_from_ctypes(ctypes.c_uint16, _Integer)
    int32 = _make_ctype_from_ctypes(ctypes.c_int32, _Integer)
    uint32 = _make_ctype_from_ctypes(ctypes.c_uint32, _Integer)
    int64 = _make_ctype_from_ctypes(ctypes.c_int64, _Integer)
    uint64 = _make_ctype_from_ctypes(ctypes.c_uint64, _Integer)


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
