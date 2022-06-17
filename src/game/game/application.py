import src.common.common as common
import src.common.common.middleware
from src.common.common.application import Application
from src.common.common.application_modules.http import HTTPServerModule
from src.common.common.application_modules.scheduler import ScheduleModule
from src.common.common.application_modules.tcp import TCPServerModule
from src.common.common.json import JsonEncoder
from src.game.game.middleware.xor import XORGameMiddleware
from src.game.game.protocol import Lineage2GameProtocol

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
