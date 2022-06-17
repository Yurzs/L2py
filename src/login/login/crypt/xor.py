import functools

from src.common.common.ctype import ctype


def xor_encrypt_login(func):
    def xor(data: bytearray, key: ctype.int32):

        stop: ctype.int32 = len(data) - 8
        start: ctype.int32 = 4
        ecx: ctype.int32 = key

        for pos in range(start, stop, 4):
            edx: ctype.int32 = data[pos] & 255
            edx |= (data[pos + 1] & 255) << 8
            edx |= (data[pos + 2] & 255) << 16
            edx |= (data[pos + 3] & 255) << 24

            ecx += edx
            edx ^= ecx

            data[pos : pos + 4] = edx

        data[-8:-4] = ecx

        return data

    @functools.wraps(func)
    def wrap(packet, session):
        data = func(packet, session)
        return xor(data, session.xor_key.key)

    return wrap


def xor_decrypt_login(func):
    def xor(raw: bytearray, key: ctype.int32):
        stop: ctype.int32 = 2
        pos: ctype.int32 = len(raw) - 12
        ecx: ctype.int32 = key

        while stop < pos:
            edx: ctype.int32 = raw[pos] & 255
            edx |= (raw[pos + 1] & 255) << 8
            edx |= (raw[pos + 2] & 255) << 16
            edx |= (raw[pos + 3] & 255) << 24

            edx ^= ecx
            ecx -= edx

            raw[pos : pos + 4] = edx
            pos -= 4

        return raw

    def wrap(packet_cls, data, *args, **kwargs):
        decrypted = xor(data, list(data[-8:-4]))
        return func(packet_cls, decrypted, *args, **kwargs)

    return wrap
