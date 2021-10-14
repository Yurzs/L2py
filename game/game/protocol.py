import logging

from common.api_handlers import handle_request
from common.packet import Packet
from common.response import Response
from common.transport.protocol import TCPProtocol
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
        request = self.transport.read(data)
        response = await handle_request(request)
        if response:
            LOG.debug(
                "Sending packet to %s:%s",
                *self.transport.peer,
            )
            self.transport.write(response)
            for action in response.actions_after:
                action_result = await action
                if isinstance(action_result, Packet):
                    self.transport.write(Response(action_result, self.session))
