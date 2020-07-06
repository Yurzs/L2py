import functools

from common.datatypes import Int32, Int8
from common.helpers.bytearray import ByteArray


def add_checksum(func):
    def _checksum(data: ByteArray):
        chksum = Int32(0)
        for i in range(0, len(data) - 8, 4):
            check = Int8(data[i]) & 0xff
            check |= Int8(data[i + 1]) << 8 & 0xff00
            check |= Int8(data[i + 2]) << 0x10 & 0xff0000
            check |= Int8(data[i + 3]) << 0x18 & 0xff000000
            chksum ^= check

        end = len(data) - 8

        data[end] = chksum & 0xff
        data[end + 1] = chksum >> 0x08 & 0xff
        data[end + 2] = chksum >> 0x10 & 0xff
        data[end + 3] = chksum >> 0x18 & 0xff

        return data

    @functools.wraps(func)
    def wrap(*args, **kwargs):
        data = func(*args, **kwargs)
        return _checksum(data)

    return wrap


def verify_checksum(func):
    def verify(data, offset, size):
        if size % 4 != 0:
            return False

        chksum = 0
        j = 0
        for i in range(offset, size - 4, 4):
            check = Int32(data[i]) & 0xff
            check |= Int32(data[i + 1] << 8) & 0xff00
            check |= Int32(data[i + 2] << 0x10) & 0xff0000
            check |= Int32(data[i + 3] << 0x18) & 0xff000000

            chksum ^= check

            j = i

        check = Int8(data[j]) & 0xff
        check |= Int8(data[j + 1]) << 8 & 0xff00
        check |= Int8(data[j + 2]) << 0x10 & 0xff0000
        check |= Int8(data[j + 3]) << 0x18 & 0xff000000

        return check == chksum

    @functools.wraps(func)
    def wrap(packet_type, data, client, *args, **kwargs):
        verify(data, 0, )
