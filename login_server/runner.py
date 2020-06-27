import asyncio

from login_server.protocol.tcp import Lineage2LoginProtocol
from login_server import packets


async def main():
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: Lineage2LoginProtocol(),
        "0.0.0.0", 2106)

    async with server:
        await server.serve_forever()


asyncio.run(main())
