import common
import login.middleware
from common.application import Application
from common.application_modules.http import HTTPServerModule
from common.application_modules.tcp import TCPServerModule
from common.json import JsonDecoder, JsonEncoder
from login.game_watcher import GameServersChecker
from login.protocol import Lineage2LoginProtocol

LOGIN_SERVER_APPLICATION = Application(
    [
        HTTPServerModule("login_web", json_encoder=JsonEncoder, json_decoder=JsonDecoder),
        TCPServerModule(
            "login_tcp",
            Lineage2LoginProtocol,
            middleware=[
                common.middleware.length.DataLengthMiddleware,
                login.middleware.EncryptionMiddleware,
                login.middleware.ChecksumMiddleware,
                login.middleware.XORMiddleware,
                login.middleware.PaddingMiddleware,
            ],
        ),
        GameServersChecker("game_checker"),
    ]
)
