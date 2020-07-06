import functools

from common.datatypes.integer import Int32, Int8, UInt32
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

            data[pos] = Int8(edx & 255)
            data[pos + 1] = Int8(edx >> 8 & 255)
            data[pos + 2] = Int8(edx >> 16 & 255)
            data[pos + 3] = Int8(edx >> 24 & 255)

        data[stop] = Int8(ecx & 0xFF)
        data[stop + 1] = Int8(ecx >> 8 & 0xFF)
        data[stop + 2] = Int8(ecx >> 16 & 0xFF)
        data[stop + 3] = Int8(ecx >> 24 & 0xFF)

        return data

    @functools.wraps(func)
    def wrap(packet, client, *args, **kwargs):
        data = func(packet, client, *args, **kwargs)
        return xor(data, client.xor_key.key)

    return wrap


def xor_encrypt_game(func):
    def xor(data, key):
        temp = Int8(0)
        print(f"data len {len(data)}, key len {len(key)}")

        for i in range(len(data)):
            temp2 = Int8(data[i] & 0xff)
            print(temp2, type(temp2), i & 15, data[i])
            data[i] = Int8(temp2 ^ (key[i & 15] & 0xff) ^ temp)
            temp = data[i]

        old = key[8] & 0xff
        old |= (key[9] << 0x08) & 0xff00
        old |= (key[10] << 0x10) & 0xff0000
        old |= (key[11] << 0x18) & 0xff000000

        old += len(data)

        key[8] = old & 0xff
        key[9] = (old >> 0x08) & 0xff
        key[10] = (old >> 0x10) & 0xff
        key[11] = (old >> 0x18) & 0xff

        return data

    def wrap(packet, client, *args, **kwargs):
        return xor(func(packet, client, *args, **kwargs), client.xor_key.encrypt_key)

    return wrap


def xor_decrypt_login(func):
    def xor(raw, key):
        stop = 4
        pos = len(raw) - 12
        ecx = UInt32(key)

        while (stop <= pos):
            edx = Int32(raw[pos] & 0xff)
            edx |= Int32((raw[pos + 1] & 0xff) << 8)
            edx |= Int32((raw[pos + 2] & 0xff) << 16)
            edx |= Int32((raw[pos + 3] & 0xff) << 24)

            edx ^= ecx
            ecx -= edx

            raw[pos] = Int8(edx & 0xff)
            raw[pos + 1] = Int8((edx >> 8) & 0xff)
            raw[pos + 2] = Int8((edx >> 16) & 0xff)
            raw[pos + 3] = Int8((edx >> 24) & 0xff)
            pos -= 4

        return raw

    def wrap(packet_cls, data, client, *args, **kwargs):
        decrypted = xor(data, client.xor_key.key)
        return func(packet_cls, decrypted, client, *args, **kwargs)

    return wrap
