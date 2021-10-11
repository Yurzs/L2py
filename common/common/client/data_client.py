from aiojsonapi.client import ApiClient


class DataClient(ApiClient):
    async def authenticate(self, login, password):
        """Requests information about account."""

        return await self.post(
            "api/data/account.authenticate",
            json_data={
                "username": login,
                "password": password,
            },
        )

    async def create_account(self, login, password, email=None):
        return await self.post(
            "login/account",
            json_data={"login": login, "password": password, "email": email},
        )

    async def delete_account(self, login):
        return await self.delete("login/account", json_data={"login": login})

    async def ban_account(self, login, duration_minutes):
        return await self.post(
            "login/account.ban",
            json_data={
                "login": login,
                "duration_minutes": duration_minutes,
            },
        )

    async def unban_account(self, login):
        return await self.post(
            "login/account.unban",
            json_data={
                "login": login,
            },
        )

    async def set_account_latest_server(self, login, server_id):
        return await self.post(
            "login/account.set_latest_server",
            json_data={"login": login, "server_id": server_id},
        )

    async def get_game_server_list(self):
        return await self.post("api/data/servers/game.list")

    async def get_server(self, _id):
        return await self.get("game/server", json_data={"id": _id})

    async def post_gameserver_ping(self, _id):
        return await self.post("game/server.ping", json_data={"id": _id})

    async def get_game_servers(self):
        return await self.post("api/data/servers/game.list")

    async def get_characters(self, login, server_id):
        return await self.post("api/data/")

    async def get_static(self, static_cls: type):
        return await self.post(f"api/static_data", {"classname": static_cls.__name__})

    async def create_character(self, character):
        return await self.post(
            "api/character.create", {"character": character}, keep_none=True
        )

    async def model_action(self, query):
        return await self.post(
            "api/data/internal/model.query",
            query,
            keep_none=True,
        )
