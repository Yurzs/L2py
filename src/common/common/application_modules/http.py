import json
import logging

from aiohttp import web

from src.common.common.application_modules.module import ApplicationModule

LOG = logging.getLogger(f"L2py.{__name__}")


class HTTPServerModule(ApplicationModule):
    """JSON HTTP application module.

    Serves web API requests.
    """

    def __init__(
        self,
        name,
        middleware=None,
        json_encoder=json.JSONEncoder,
        json_decoder=json.JSONDecoder,
    ):
        super().__init__(name)
        self.middleware = middleware
        self.json_encoder = json_encoder
        self.json_decoder = json_decoder

    def start(self, config, loop):
        from aiojsonapi.config import config as aioconfig
        from aiojsonapi.routes import routes

        aioconfig.json_encoder = self.json_encoder
        aioconfig.json_decoder = self.json_decoder

        app = web.Application(middlewares=self.middleware)
        app.add_routes(routes)
        runner = web.AppRunner(app)

        loop.run_until_complete(runner.setup())
        site = web.TCPSite(runner, config["host"], config["port"])
        LOG.info("Starting Web server on %s:%s", config["host"], config["port"])
        loop.run_until_complete(site.start())
