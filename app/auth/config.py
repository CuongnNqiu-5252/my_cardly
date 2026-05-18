# src.auth.config
from datetime import timedelta
from app.constants import environment
from pydantic_settings import BaseSettings


class AuthConfig(BaseSettings):
    ALGORITHM: str = environment.ALGORITHM
    SECRET_KEY: str = environment.SECRET_KEY
    ACCESS_TOKEN_EXPIRES_MINUTES : int = environment.ACCESS_TOKEN_EXPIRES_MINUTES
    # REFRESH_TOKEN_KEY: str
    # REFRESH_TOKEN_EXP: timedelta = timedelta(days=30)

    SECURE_COOKIES: bool = True


auth_settings = AuthConfig()


