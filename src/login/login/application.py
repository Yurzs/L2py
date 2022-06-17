import src.common.common as common
import src.common.common.middleware.length
import src.login.login.middleware
import src.login.login as login
from src.common.common.application import Application
from src.common.common.application_modules.http import HTTPServerModule
from src.common.common.application_modules.tcp import TCPServerModule
from src.common.common.json import JsonDecoder, JsonEncoder
from src.login.login.protocol import Lineage2LoginProtocol

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
    ]
)
