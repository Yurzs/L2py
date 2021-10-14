import aiohttp

from common import exceptions


class ApiClient:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port

    def _delete_none(self, request: dict):
        """Removes None values from request."""

        return {key: value for key, value in request.items() if value is not None}

    def _format_path(self, endpoint):
        return f"http://{self.server_ip}:{self.server_port}/{endpoint}"

    async def _make_request(self, endpoint, method, json_data=None):
        url = self._format_path(endpoint)
        async with aiohttp.ClientSession() as session:
            _method = getattr(session, method)
            async with _method(url, json=self._delete_none(json_data or {})) as response:
                result = await response.json()
                if result["error"]:
                    if isinstance(result["reason"], dict):
                        if hasattr(exceptions, result["reason"]["code"]):
                            exc = getattr(exceptions, result["reason"]["code"])
                        else:
                            exc = exceptions.ApiException
                        raise exc(result["reason"]["text"])
                    else:
                        raise exceptions.ApiException(result["reason"])
                else:
                    return result["result"]

    async def get(self, endpoint, json_data=None):
        return await self._make_request(endpoint, "get", json_data=json_data)

    async def post(self, endpoint, json_data=None):
        return await self._make_request(endpoint, "post", json_data=json_data)

    async def delete(self, endpoint, json_data=None):
        return await self._make_request(endpoint, "delete", json_data=json_data)

    async def put(self, endpoint, json_data=None):
        return await self._make_request(endpoint, "put", json_data=json_data)

    async def patch(self, endpoint, json_data=None):
        return await self._make_request(endpoint, "patch", json_data=json_data)
