from aiojsonapi.client import ApiClient


class GameClient(ApiClient):
    async def ping(self):
        return await self.post("api/ping")
