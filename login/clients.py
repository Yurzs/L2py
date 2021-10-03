from common.client.data_client import DataClient
from common.json import JsonDecoder, JsonEncoder
from login.config import DATA_SERVER_IP, DATA_SERVER_PORT

data_client = DataClient(
    server_ip=DATA_SERVER_IP,
    server_port=DATA_SERVER_PORT,
    json_decoder=JsonDecoder,
    json_encoder=JsonEncoder,
    https=False,
)
