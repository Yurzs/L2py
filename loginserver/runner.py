import logging
import sys

import aiohttp.web
from aiojson.middleware import error_middleware
from aiojson.routes import routes

from loginserver import api
from loginserver.config import loop
from loginserver.manager import LoginServerPacketManager
from loginserver.protocol.outer import Lineage2LoginProtocol

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


async def start_api(host, port):
    api  # for code reformat
    router = aiohttp.web.UrlDispatcher()
    router.add_routes(routes)
    app = aiohttp.web.Application(loop=loop, router=router, middlewares=[error_middleware])
    runner = aiohttp.web.AppRunner(app)
    await runner.setup()
    site = aiohttp.web.TCPSite(runner, host=host, port=port)
    await site.start()


async def main():
    server = await loop.create_server(
        lambda: Lineage2LoginProtocol(loop, LoginServerPacketManager),
        "0.0.0.0", 2106)
    await start_api("0.0.0.0", 2107)

    async with server:
        await server.serve_forever()


loop.run_until_complete(main())
