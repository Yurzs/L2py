import logging

from common.api_handlers import handle_request
from common.transport.protocol import TCPProtocol

from game.config import GameConfig
from game.session import GameSession
from game.states import Connected

LOG = logging.getLogger(f"l2py.{__name__}")


class Lineage2GameProtocol(TCPProtocol):
    session_cls = GameSession

    def connection_made(self, transport):
        super().connection_made(transport)

        LOG.info(
            "New connection from %s:%s",
            *self.transport.peer,
        )
        self.session.set_state(Connected)

    @TCPProtocol.make_async
    async def data_received(self, data: bytes):
        for request in self.transport.read(data):
            GameConfig().loop.create_task(self.proceed_request(request))

    async def proceed_request(self, request):
        response = await handle_request(request)
        if response:
            LOG.debug(
                "Sending packet to %s:%s",
                *self.transport.peer,
            )
            self.transport.write(response)

    def connection_lost(self, exc) -> None:
        self.session.logout_character()
