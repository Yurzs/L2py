import logging

from src.common.common.ctype import ctype
from src.common.common.request import Request
from src.common.common.response import Response

LOG = logging.getLogger(f"l2py.{__name__}")


class PacketTransport:
    def __init__(self, transport, session, middleware):
        self._transport = transport
        self.session = session
        self.middleware = middleware

    @property
    def peer(self):
        return self._transport.get_extra_info("peername")

    def read(self, data: bytes, request_cls: type = Request):
        data = bytearray(data)
        requests = []
        while True:
            if data:
                packet_len: ctype.int16 = int.from_bytes(data[0:2], "big")
                request = request_cls(raw_data=data[:packet_len], session=self.session)
                requests.append(request)
                data = data[packet_len:]
                for middleware in self.middleware:
                    middleware.before(self.session, request)
            else:
                break
        return requests

    def write(self, response: Response):
        for middleware in self.middleware[::-1]:
            middleware.after(self.session, response)
        LOG.debug(f"SENDING: %s %s", response.packet, len(bytes(response.data)))
        LOG.debug(bytes(response.data))
        return self._transport.write(bytes(response.data))

    def close(self):
        return self._transport.close()
