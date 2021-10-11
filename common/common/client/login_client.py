import json

from aiojsonapi.client import ApiClient


class LoginClient(ApiClient):
    async def auth_login(self, login, login_ok1, login_ok2, play_ok1, play_ok2):
        return await self.post(
            "api/login/auth_login",
            json_data={
                "login": login,
                "login_ok1": login_ok1,
                "login_ok2": login_ok2,
                "play_ok1": play_ok1,
                "play_ok2": play_ok2,
            },
        )
