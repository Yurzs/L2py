from common.adapter import DataAdapter
from common.client.data_client import DataClient


class _HttpCollection:
    def __init__(
        self, data_client: DataClient, database_name: str, collection_name: str
    ):
        self.data_client = data_client
        self.database_name = database_name
        self.collection_name = collection_name

    def fake_func(self, action: str):
        async def wrap(*args, **kwargs):
            return await self.data_client.model_action(
                {
                    "database": self.database_name,
                    "collection": self.collection_name,
                    "action": action,
                    "args": args,
                    "kwargs": kwargs,
                }
            )

        return wrap

    def __getattr__(self, item):
        return self.fake_func(item)


class HttpAdapter(DataAdapter):
    def __init__(self, data_client: DataClient):
        self.data_client = data_client

    def client(self):
        raise NotImplementedError

    def collection(self, database_name, collection_name):
        return _HttpCollection(self.data_client, database_name, collection_name)

    def database(self, database_name):
        raise NotImplementedError
