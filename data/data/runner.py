import common  # noqa: F401
import data.api  # noqa: F401
from common.document import register_adapter
from data import config
from data.application import DATA_SERVER_APPLICATION
from data.models.adapters.mongo import MongoAdapter


def main():
    register_adapter(MongoAdapter(config.MONGO_URI))
    DATA_SERVER_APPLICATION.run(
        {
            "data_web": {
                "host": config.DATA_SERVER_HOST,
                "port": config.DATA_SERVER_PORT,
            }
        }
    )


if __name__ == "__main__":
    main()
