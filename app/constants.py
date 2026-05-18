import os

from dotenv import load_dotenv
from pydantic import ConfigDict
from pydantic_settings import BaseSettings



class Environment(BaseSettings):
    GOOGLE_CLIENT_ID : str
    GOOGLE_CLIENT_SECRET : str
    GOOGLE_REDIRECT_URI :str

    ALGORITHM : str
    SECRET_KEY: str
    MONGO_HOST : str
    ACCESS_TOKEN_EXPIRES_MINUTES : str
    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )

environment = Environment()