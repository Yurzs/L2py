from common.client.client import ApiClient

from gameserver.config import login_server_ip


class LoginClient(ApiClient):
    path = "game"

    def __init__(self, server_ip=None):
        server_ip = server_ip if server_ip else login_server_ip
        super().__init__(server_ip)

    async def auth_login(self, login, login_ok1, login_ok2, play_ok1, play_ok2):
        return await self._make_request("auth_login", json_data={
            "login": login.value,
            "login_ok1": login_ok1.value,
            "login_ok2": login_ok2.value,
            "play_ok1": play_ok1.value,
            "play_ok2": play_ok2.value,
        })
