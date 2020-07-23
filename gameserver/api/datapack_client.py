from common.client.client import ApiClient
from gameserver.config import data_server_ip


class DataPackClient(ApiClient):
    path = "data"

    def __init__(self, server_ip=None):
        server_ip = server_ip if server_ip else data_server_ip
        super().__init__(server_ip)

    async def get_classes(self):
        return await self._make_request("classes")

    async def get_npcs(self):
        return await self._make_request("npcs")

    async def get_announcements(self):
        return await self._make_request("announcements")

    async def get_regions(self):
        return await self._make_request("regions")
