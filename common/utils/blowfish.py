import functools


def blowfish_encrypt(init=False):
    def inner(func):
        @functools.wraps(func)
        def wrap(packet, client, *args, **kwargs):
            data = func(packet, client, *args, **kwargs)
            encrypted = client.blowfish_key.encrypt(data, init)
            return encrypted

        return wrap

    return inner


def blowfish_decrypt(func):
    @functools.wraps(func)
    def wrap(packet_cls, data, client, *args, **kwargs):
        if not args:
            data.reverse()
            decoded = client.blowfish_key.decrypt(data)
            return func(packet_cls, decoded, client, **kwargs)
        return func(packet_cls, data, client, *args, **kwargs)

    return wrap
