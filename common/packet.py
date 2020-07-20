import functools
from collections import OrderedDict

from common.datatypes import Int16, Int8
from common.helpers.bytearray import ByteArray
from common.utils.blowfish import blowfish_decrypt
from abc import ABCMeta, abstractmethod


class UnknownPacket(Exception):
    pass


def add_length(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        packet = func(*args, **kwargs)
        packed_size = Int16(2 + len(packet)).encode()
        return packed_size + packet

    return wrap


def add_padding(xor_key=False):
    def inner(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            data = func(*args, **kwargs)
            pad_length = 4
            if xor_key:
                pad_length += 4
            pad_length += 8 - (len(data) + pad_length) % 8
            data.pad(pad_length)
            return data

        return wrap

    return inner


class MetaPacket(ABCMeta):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.mapper = {}


class Packet(metaclass=MetaPacket):
    type: Int8
    arg_order: OrderedDict

    @abstractmethod
    def encode(self, client):
        pass

    @property
    def body(self):
        data = ByteArray(b"")
        for arg in self.arg_order:
            data.extend(getattr(self, arg).encode())
        return data

    @classmethod
    @abstractmethod
    def parse(cls, data, client):
        pass

    @classmethod
    @blowfish_decrypt
    def decode(cls, data, client, **kwargs):
        packet_type = data[0]
        packet_cls = cls.mapper.get(packet_type)
        if packet_cls:
            return packet_cls.parse(data, client)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __init_subclass__(cls, **kwargs):
        if hasattr(cls, "type"):
            cls.mapper[cls.type] = cls
