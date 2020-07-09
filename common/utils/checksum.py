import functools

from common.datatypes import Int32, Int8, Int64
from common.helpers.bytearray import ByteArray


def add_checksum(func):
    def _checksum(data: ByteArray):
        chksum = Int64(0)

        for i in range(0, len(data) - 4, 4):
            check = Int32(data[i]) & 0xff
            check |= Int32(data[i + 1]) << 8 & 0xff00
            check |= Int32(data[i + 2]) << 0x10 & 0xff0000
            check |= Int32(data[i + 3]) << 0x18 & 0xff000000

            chksum ^= check

        end = len(data) - 4

        data[end] = Int8(chksum & 0xff)
        data[end + 1] = Int8(chksum >> 0x08) & 0xff
        data[end + 2] = Int8(chksum >> 0x10) & 0xff
        data[end + 3] = Int8(chksum >> 0x18) & 0xff

        return data

    @functools.wraps(func)
    def wrap(*args, **kwargs):
        data = func(*args, **kwargs)
        return _checksum(data)

    return wrap


def verify_checksum(func):
    def verify(data):
        if len(data) % 4 != 0:
            return False

        chksum = Int64(0)
        j = 0
        for i in range(0, len(data) - 4, 4):
            check = Int32(data[i]) & 0xff
            check |= Int32(data[i + 1] << 8) & 0xff00
            check |= Int32(data[i + 2] << 0x10) & 0xff0000
            check |= Int32(data[i + 3] << 0x18) & 0xff000000

            chksum ^= check

        end = len(data) - 4

        check = Int8(data[end]) & 0xff
        check |= Int8(data[end + 1] << 8) & 0xff00
        check |= Int8(data[end + 2] << 0x10) & 0xff0000
        check |= Int8(data[end + 3] << 0x18) & 0xff000000

        return check == chksum

    @functools.wraps(func)
    def wrap(packet_type, data, client, *args, **kwargs):
        # if verify(data):

        return func(packet_type, data, client, *args, **kwargs)
        # verify(data)
        # return data
    return wrap
