import logging

import login.session
from common.api_handlers import handle_request
from common.response import Response
from common.transport.protocol import TCPProtocol
from login.packets import Init
from login.state import Connected

LOG = logging.getLogger(f"l2py.{__name__}")


class Lineage2LoginProtocol(TCPProtocol):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.session_cls = login.session.LoginSession

    def connection_made(self, transport):
        super().connection_made(transport)

        LOG.debug(
            "New connection from %s:%s",
            *self.transport.peer,
        )

        response = Response(
            packet=Init(
                session_id=self.session.id,
                protocol_version=self.session.protocol_version,
                rsa_key=self.session.rsa_key.scramble_mod(),
                blowfish_key=self.session.blowfish_key.key,
            ),
            session=self.session,
        )
        self.transport.write(response)
        self.session.blowfish_enabled = True
        self.session.set_state(Connected)

    @TCPProtocol.make_async
    async def data_received(self, data: bytes):
        for request in self.transport.read(data):
            response = await handle_request(request)
            if response:
                LOG.debug(
                    "Sending packet to %s:%s",
                    *self.transport.peer,
                )
                self.transport.write(response)

    def connection_lost(self, exc) -> None:
        super().connection_lost(exc)
        # self.session.delete()
        LOG.debug(
            "Connection lost to %s:%s",
            *self.transport.peer,
        )
