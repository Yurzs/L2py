class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class _ClassProperty:
    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, cls=None):
        if cls is None:
            cls = type(obj)
        return self.fget.__get__(obj, cls)()

    def __set__(self, obj, value):
        if not self.fset:
            raise AttributeError("can't set attribute")

        cls = type(obj)
        return self.fset.__get__(obj, cls)(value)

    def setter(self, func):
        if not isinstance(func, (classmethod, staticmethod)):
            func = classmethod(func)
        self.fset = func
        return self


def classproperty(func):
    if not isinstance(func, (classmethod, staticmethod)):
        func = classmethod(func)
    return _ClassProperty(func)


UTF8 = "utf-8"
UTF16LE = "utf-16-le"


def decode_str(encoding=UTF16LE):
    def inner_decode(data: bytearray):
        if encoding == UTF16LE:
            for chunk in data.split(b"\x00\x00"):
                if len(chunk) % 2:
                    chunk += b"\x00"
                result = chunk.decode(encoding=encoding)
                return result, len(chunk) + 2
        elif encoding == UTF8:
            result = data.rstrip(b"\x00").decode(encoding=encoding)
            return data.rstrip(b"\x00").decode(encoding=encoding), len(result) + 1
        else:
            raise TypeError()

    return inner_decode


def encode_str(text, encoding=UTF16LE):
    return text.encode(encoding) + b"\x00\x00"


def extend_bytearray(array: bytearray, ctype_data):
    for item in ctype_data:
        if isinstance(item, str):
            item = encode_str(item)
        array.extend(bytes(item))
