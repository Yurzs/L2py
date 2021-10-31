import logging

from common.helpers.bytearray import ByteArray
from common.request import Request
from common.response import Response

LOG = logging.getLogger(f"l2py.{__name__}")


class PacketTransport:
    def __init__(self, transport, session, middleware):
        self._transport = transport
        self.session = session
        self.middleware = middleware

    @property
    def peer(self):
        return self._transport.get_extra_info("peername")

    def read(self, data):
        data = ByteArray(data)
        requests = []
        while True:
            if data:
                packet_len = int(Int16(data[0:2]))
                request = Request(data[:packet_len], self.session)
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
        LOG.debug(f"SENDING: %s", response.packet)
        return self._transport.write(bytes(response.data))

    def close(self):
        return self._transport.close()
