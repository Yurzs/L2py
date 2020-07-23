import aiohttp


class ApiClient:
    path: str

    def __init__(self, server_ip):
        self.server_ip = server_ip

    def _format_path(self, endpoint):
        return f"http://{self.server_ip}:2107/{self.path}/{endpoint}"

    async def _make_request(self, endpoint, json_data=None):
        url = self._format_path(endpoint)
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=json_data or {}) as response:
                result = await response.json()
                if result["error"]:
                    if result["error"].get("text"):
                        raise Exception(result["reason"]["text"])
                    else:
                        raise Exception(result["reason"])
                else:
                    return result["result"]
