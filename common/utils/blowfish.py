import functools
import logging

LOG = logging.getLogger(f"l2py.{__name__}")


def blowfish_encrypt(init=False):
    def inner(func):
        @functools.wraps(func)
        def wrap(packet, client, *args, **kwargs):
            data = func(packet, client, *args, **kwargs)
            print(data.data)
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
            LOG.debug(f"Decoded client packet: %s\nIn bytes %s", decoded, decoded.data)
            return func(packet_cls, decoded, client, **kwargs)
        return func(packet_cls, data, client, *args, **kwargs)

    return wrap
