from common.datatypes import Int32, Int8


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