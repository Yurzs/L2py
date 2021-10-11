import common
from common.application import Application
from common.application_modules.http import HTTPServerModule
from common.application_modules.scheduler import ScheduleModule
from common.application_modules.tcp import TCPServerModule
from common.json import JsonEncoder
from game.middleware.xor import XORGameMiddleware
from game.protocol import Lineage2GameProtocol

GAME_SERVER_APPLICATION = Application(
    [
        TCPServerModule(
            "game_tcp",
            Lineage2GameProtocol,
            middleware=[
                common.middleware.length.DataLengthMiddleware,
                XORGameMiddleware,
            ],
        ),
        HTTPServerModule("game_web", json_encoder=JsonEncoder),
        ScheduleModule(),
    ]
)
