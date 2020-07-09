from gameserver.config import loop
from gameserver.protocol.outer import Lineage2GameProtocol
from gameserver.manager import GameServerPacketManager


async def main():
    server = await loop.create_server(
        lambda: Lineage2GameProtocol(loop, GameServerPacketManager),
        "0.0.0.0", 7777)

    async with server:
        await server.serve_forever()


loop.run_until_complete(main())
