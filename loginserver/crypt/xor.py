import functools

from common.datatypes import Int32
from common.helpers.bytearray import ByteArray


def xor_encrypt_login(func):
    def xor(data: ByteArray, key):
        stop = len(data) - 8
        start = 4
        ecx = Int32(key)

        for pos in range(start, stop, 4):
            edx = (Int32(data[pos]) & 255)
            edx |= (Int32(data[pos + 1]) & 255) << 8
            edx |= (Int32(data[pos + 2]) & 255) << 16
            edx |= (Int32(data[pos + 3]) & 255) << 24

            ecx += edx
            edx ^= ecx

            data[pos: pos+4] = edx

        data[-8:-4] = ecx

        return data

    @functools.wraps(func)
    def wrap(packet, client, *args, **kwargs):
        data = func(packet, client, *args, **kwargs)
        return xor(data, client.xor_key.key)

    return wrap


def xor_decrypt_login(func):
    def xor(raw, key):
        stop = 2
        pos = len(raw) - 12
        ecx = Int32(key)

        while stop < pos:
            edx = (Int32(raw[pos]) & 255)
            edx |= (Int32(raw[pos + 1]) & 255) << 8
            edx |= (Int32(raw[pos + 2]) & 255) << 16
            edx |= (Int32(raw[pos + 3]) & 255) << 24

            edx ^= ecx
            ecx -= edx

            raw[pos: pos+4] = edx
            pos -= 4

        return raw

    def wrap(packet_cls, data, *args, **kwargs):
        decrypted = xor(data, list(data[-8: -4]))
        return func(packet_cls, decrypted, *args, **kwargs)

    return wrap