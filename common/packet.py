from .datatypes import Short
from abc import ABCMeta, abstractmethod
from common.datatypes import Short, Int, Bytes
from collections import OrderedDict
import struct


class UnknownPacket(Exception):
    pass


class Packet:
    type: int
    data: OrderedDict

    @property
    def encoded(self):
        encoded_params = b"".join([data.encode() for data in self.data.values()])
        if 3 + len(encoded_params) < 255:
            packed_size = Bytes((3 + len(encoded_params)).to_bytes(1, "big") + b"\x00").encode()
        else:
            packed_size = Short(3 + len(encoded_params)).encode()
        return b"".join([
            packed_size,
            self.type.to_bytes(1, "big"),
            encoded_params
        ])

    @property
    def checksum(self):
        chksum = 0
        data = self.encoded
        for i in range(0, len(data), 4):
            check = data[i] & 0xff
            check |= data[i + 1] << 8 & 0xff00
            check |= data[i + 2] << 0x10 & 0xff0000
            check |= data[i + 3] << 0x18 & 0xff000000
            chksum ^= check

        return struct.pack("!L", chksum)

    def verify_checksum(self, data, offset, size):
        if size % 4 != 0:
            return False

        data = list(struct.unpack("!{}".format("b" * len(data)), data))
        chksum = 0
        j = 0
        for i in range(offset, size - 4, 4):
            check = data[i] & 0xff
            check |= data[i + 1] << 8 & 0xff00
            check |= data[i + 2] << 0x10 & 0xff0000
            check |= data[i + 3] << 0x18 & 0xff000000

            chksum ^= check

            j = i

        check = data[j] & 0xff
        check |= data[j + 1] << 8 & 0xff00
        check |= data[j + 2] << 0x10 & 0xff0000
        check |= data[j + 3] << 0x18 & 0xff000000

        return check == chksum

    @property
    def encoded_with_checksum(self):
        result = self.encoded
        checksum = self.checksum
        pad_len = (8 - (len(result) + len(checksum)) % 8) % 8
        return self.encoded + self.checksum + pad_len * b"\x00"

    @classmethod
    @abstractmethod
    def parse(cls, packet_len, packet_type, data):
        pass

    @classmethod
    def decode(cls, data, packet_len=None, packet_type=None):
        if not packet_len and not packet_type:
            packet_len = Short.decode(data[0:2])
            packet_type = data[3]
            data = data[3:]

        packet_cls: Packet = None
        for sub in cls.__subclasses__():
            print(sub.type, packet_type )
            if sub.type == packet_type:
                packet_cls = sub
                break
            else:
                result = sub.decode(data, packet_len, packet_type)
                if result:
                    return result
        if packet_cls:
            return packet_cls.parse(packet_len, packet_type, data)