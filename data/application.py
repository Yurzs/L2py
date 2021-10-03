from common.application import Application
from common.application_modules.http import HTTPServerModule
from common.json import JsonEncoder

DATA_SERVER_APPLICATION = Application(
    [HTTPServerModule("data_web", json_encoder=JsonEncoder)]
)
