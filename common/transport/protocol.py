import asyncio
import functools
import logging
from abc import ABCMeta, abstractmethod
from asyncio import transports

from common.helpers.bytearray import ByteArray
from common.datatypes import Int16

log = logging.getLogger("l2common." + __name__)


class TCPProtocol(asyncio.Protocol, metaclass=ABCMeta):
    def __init__(self, loop, manager_cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loop = loop
        self.manager = manager_cls()

    @staticmethod
    def make_async(func):
        @functools.wraps(func)
        async def async_wrap(protocol, data):
            return await func(protocol, data)

        @functools.wraps(func)
        def wrap(protocol, data):
            return asyncio.Task(async_wrap(protocol, data), loop=protocol.loop)
        return wrap

    @staticmethod
    def data_to_bytearray(func):
        async def wrap(protocol, data):
            data = ByteArray(data)
            data.reverse()
            packet_len = Int16(data[-2:]) - 2
            data = ByteArray(data[:-2])
            if not packet_len == len(data):
                log.error("Data len byte doesnt match data length.")
            return await func(protocol, data)
        return wrap

    @abstractmethod
    async def data_received(self, data: ByteArray) -> None:
        pass


class InnerTCPProtocol(asyncio.Protocol):
    def __init__(self, loop, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loop = loop

    def connection_made(self, transport: transports.BaseTransport) -> None:
        self.transport = transport

    @abstractmethod
    async def data_received(self, data: bytes) -> None:
        pass

    def write(self, data):
        self.transport.write(data)
