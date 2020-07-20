import functools
import logging

from common.datatypes import Int32, Int8, Int64
from common.helpers.bytearray import ByteArray


LOG = logging.getLogger(f"l2py.{__name__}")


def add_checksum(func):
    def _checksum(data: ByteArray):
        chksum = Int32(0)

        for i in range(0, len(data) - 4, 4):
            check = Int32(data[i]) & 0xff
            check |= Int32(data[i + 1]) << 8 & 0xff00
            check |= Int32(data[i + 2]) << 0x10 & 0xff0000
            check |= Int32(data[i + 3]) << 0x18 & 0xff000000

            chksum ^= check

        data[-4:] = chksum

        return data

    @functools.wraps(func)
    def wrap(*args, **kwargs):
        data = func(*args, **kwargs)
        data = _checksum(data)
        verify(data)
        return data
    return wrap


def verify_checksum(func):

    @functools.wraps(func)
    def wrap(packet_type, data, *args, **kwargs):
        if verify(data):
            return func(packet_type, data, *args, **kwargs)
        else:
            LOG.warning("Wrong checksum from client")
    return wrap


def verify(data):
    if len(data) % 4 != 0:
        return False

    chksum = Int32(0)
    for i in range(0, len(data) - 4, 4):
        check = Int32(data[i]) & 0xff
        check |= Int32(data[i + 1]) << 8 & 0xff00
        check |= Int32(data[i + 2]) << 0x10 & 0xff0000
        check |= Int32(data[i + 3]) << 0x18 & 0xff000000

        chksum ^= check

    check = Int32(data[-4:])

    return check == chksum
