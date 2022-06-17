import asyncio
import functools
import logging
from abc import ABCMeta, abstractmethod
from asyncio import transports

from src.common.common.request import Request
from src.common.common.response import Response
from src.common.common.session import Session
from src.common.common.transport.packet_transport import PacketTransport

LOG = logging.getLogger("l2py." + __name__)


class TCPProtocol(asyncio.Protocol, metaclass=ABCMeta):
    session_cls: type = Session
    session: session_cls
    request_cls: type = Request
    response_cls: type = Response
    transport: PacketTransport

    def __init__(self, loop, middleware, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loop = loop
        self.middleware = middleware

    @staticmethod
    def make_async(func):
        @functools.wraps(func)
        async def async_wrap(protocol, data):
            return await func(protocol, data)

        @functools.wraps(func)
        def wrap(protocol, data):
            return asyncio.Task(async_wrap(protocol, data), loop=protocol.loop)

        return wrap

    def connection_made(self, transport: transports.BaseTransport) -> None:
        self.session = self.session_cls(self)
        self.transport = PacketTransport(transport, self.session, self.middleware)

    @abstractmethod
    async def data_received(self, data: bytes) -> None:
        pass
