import os

MONGO_URI = os.environ["MONGO_URI"]

DATA_SERVER_HOST = os.environ.get("DATA_SERVER_HOST", "0.0.0.0")
DATA_SERVER_PORT = os.environ.get("DATA_SERVER_PORT", 2108)
