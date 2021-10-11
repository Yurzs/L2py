from common.application import Application
from common.application_modules.http import HTTPServerModule
from common.json import JsonDecoder, JsonEncoder

DATA_SERVER_APPLICATION = Application(
    [HTTPServerModule("data_web", json_encoder=JsonEncoder, json_decoder=JsonDecoder)]
)
