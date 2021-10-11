from common.client.data_client import DataClient
from common.json import JsonDecoder, JsonEncoder
from login.config import DATA_SERVER_HOST, DATA_SERVER_PORT

DATA_CLIENT = DataClient(
    server_ip=DATA_SERVER_HOST,
    server_port=DATA_SERVER_PORT,
    json_decoder=JsonDecoder,
    json_encoder=JsonEncoder,
    https=False,
)
