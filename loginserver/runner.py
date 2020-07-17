import logging
import sys

from loginserver.config import loop
from loginserver.protocol.outer import Lineage2LoginProtocol
from loginserver.manager import LoginServerPacketManager

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


async def main():
    server = await loop.create_server(
        lambda: Lineage2LoginProtocol(loop, LoginServerPacketManager),
        "0.0.0.0", 2106)

    async with server:
        await server.serve_forever()


loop.run_until_complete(main())
