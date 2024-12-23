from pymongo import MongoClient
from .config import Config

def get_db():
    """Підключення до MongoDB."""
    client = MongoClient(Config.MONGO_URI)
    return client[Config.DATABASE_NAME]
