from common.client.client import ApiClient
from gameserver.config import data_server_api_ip, data_server_api_port


class DataPackClient(ApiClient):
    path = "data"

    def __init__(self, server_ip=None, server_port=None):
        server_ip = server_ip if server_ip else data_server_api_ip
        server_port = server_port if server_port else data_server_api_port
        super().__init__(server_ip, server_port)

    async def get_classes(self):
        return await self._make_request("classes")

    async def get_npcs(self):
        return await self._make_request("npcs")

    async def get_announcements(self):
        return await self._make_request("announcements")

    async def get_regions(self):
        return await self._make_request("regions")
