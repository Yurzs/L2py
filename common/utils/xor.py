import functools

from common.datatypes.integer import Int32, Int8
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


def xor_encrypt_game(func):
    def xor(data, key):
        temp = Int32(0)

        for i in range(len(data)):
            temp2 = Int32(data[i] & 0xff)
            data[i] = Int8(temp2 ^ key[i & 15] ^ temp)
            temp = data[i]

        old = Int32(key[8] & 0xff)
        old |= Int32(key[9] << 0x08) & 0xff00
        old |= Int32(key[10] << 0x10) & 0xff0000
        old |= Int32(key[11] << 0x18) & 0xff000000

        old += Int32(len(data))

        key[8:12] = old

        return data

    def wrap(packet, client, *args, **kwargs):
        if client.encryption_enabled:
            result = xor(func(packet, client, *args, **kwargs), client.xor_key.outgoing_key)
        else:
            result = func(packet, client, *args, **kwargs)
        return result
    return wrap


def xor_decrypt_game(func):
    def dexor(data, key):
        temp1 = Int32(0)
        for i in range(len(data)):
            temp2 = Int32(data[i]) & 0xff
            data[i] = Int8(temp2 ^ key[i & 15] ^ temp1)
            temp1 = temp2

        old = (Int32(key[8]) & 0xff)
        old |= (Int32(key[9]) << 0x08) & 0xff00
        old |= (Int32(key[10]) << 0x10) & 0xff0000
        old |= (Int32(key[11]) << 0x18) & 0xff000000

        old += Int32(len(data))

        key[8:12] = old
        return data

    def wrap(packet_cls, data, client, *args, **kwargs):
        if client.encryption_enabled:
            decrypted = dexor(data, client.xor_key.incoming_key)
            return func(packet_cls, decrypted, client, *args, **kwargs)
        else:
            return func(packet_cls, data, client, *args, **kwargs)
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
