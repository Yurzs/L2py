import logging
import sys

import aiohttp.web
from aiojson.middleware import error_middleware
from aiojson.routes import routes

from loginserver import api
from loginserver.config import loop, server_info, server_api_info
from loginserver.manager import LoginServerPacketManager
from loginserver.protocol.outer import Lineage2LoginProtocol

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

LOG = logging.getLogger(f"L2py-server-login")


async def start_api(api_host, api_port):
    api  # for code reformat
    app = aiohttp.web.Application(middlewares=[error_middleware])
    app.add_routes(routes)
    runner = aiohttp.web.AppRunner(app)
    await runner.setup()
    site = aiohttp.web.TCPSite(runner, host=api_host, port=api_port)
    LOG.info(f"Starting API server on %s:%s", api_host, api_port)
    await site.start()


async def main(host, port, api_host, api_port):
    server = await loop.create_server(
        lambda: Lineage2LoginProtocol(loop, LoginServerPacketManager),
        host, port)
    await start_api(api_host, api_port)

    LOG.info(f"Starting L2 login server on %s:%s", host, port)
    async with server:
        await server.serve_forever()


loop.run_until_complete(main(*server_info, *server_api_info))
