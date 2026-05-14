import os

from dotenv import load_dotenv

load_dotenv()


class Environment:
    POSTGRES_USER = "postgres"
    POSTGRES_PASSWORD = ""
    POSTGRES_HOST = "localhost"
    POSTGRES_PORT = "5432"
    POSTGRES_DB = "postgres"
    REDIS_HOST = "localhost"
    REDIS_PORT = "6379"
    REDIS_DB = "redis"
    REDIS_PASSWORD = ""
    REDIS_URL = "redis://localhost"
    MONGO_HOST = os.getenv('uri')