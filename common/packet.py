from abc import abstractmethod
import functools
from abc import abstractmethod
from collections import OrderedDict

from common.datatypes import Int16, Int8
from common.helpers.bytearray import ByteArray
from common.utils.blowfish import blowfish_decrypt, blowfish_encrypt
from common.utils.checksum import add_checksum


class UnknownPacket(Exception):
    pass


def add_length(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        packet = func(*args, **kwargs)
        packet.reverse()
        packed_size = Int16(2 + len(packet)).encode()
        return packet + packed_size

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


class Packet:
    type: Int8
    arg_order: OrderedDict

    @add_length
    @blowfish_encrypt()
    @add_checksum
    @add_padding()
    def encode(self, client):
        return self.body

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
    def decode(cls, data, client, packet_len, packet_type=None):
        if not packet_type:
            packet_type = data[0]
            # data = data[1:]

        packet_cls: Packet = None
        for sub in cls.__subclasses__():
            if sub.type == packet_type:
                packet_cls = sub
                break
            else:
                result = sub.decode(data, client, packet_len, packet_type)
                if result:
                    return result
        if packet_cls:
            return packet_cls.parse(data, client)
