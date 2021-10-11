from common.client.data_client import DataClient
from common.client.login_client import LoginClient
from common.json import JsonDecoder, JsonEncoder
from game.config import (
    DATA_SERVER_HOST,
    DATA_SERVER_PORT,
    LOGIN_SERVER_API_HOST,
    LOGIN_SERVER_API_PORT,
)

LOGIN_CLIENT = LoginClient(
    LOGIN_SERVER_API_HOST,
    LOGIN_SERVER_API_PORT,
    https=False,
    json_decoder=JsonDecoder,
    json_encoder=JsonEncoder,
)

DATA_CLIENT = DataClient(
    server_ip=DATA_SERVER_HOST,
    server_port=DATA_SERVER_PORT,
    json_decoder=JsonDecoder,
    json_encoder=JsonEncoder,
    https=False,
)
