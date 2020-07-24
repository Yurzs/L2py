from common.client.client import ApiClient

from gameserver.config import login_server_api_ip, login_server_api_port


class LoginClient(ApiClient):
    path = "game"

    def __init__(self, server_ip=None, server_port=None):
        server_ip = server_ip if server_ip else login_server_api_ip
        server_port = server_port if server_port else login_server_api_port
        super().__init__(server_ip, server_port)

    async def auth_login(self, login, login_ok1, login_ok2, play_ok1, play_ok2):
        return await self._make_request("auth_login", json_data={
            "login": login.value,
            "login_ok1": login_ok1.value,
            "login_ok2": login_ok2.value,
            "play_ok1": play_ok1.value,
            "play_ok2": play_ok2.value,
        })
