import data.api  # noqa: F401
from data.application import DATA_SERVER_APPLICATION


def main():
    DATA_SERVER_APPLICATION.run(
        {
            "data_web": {
                "host": "localhost",
                "port": 2108,
            }
        }
    )


if __name__ == "__main__":
    main()
