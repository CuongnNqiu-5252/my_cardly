# src.auth.config
from datetime import timedelta

from pydantic_settings import BaseSettings


class AuthConfig(BaseSettings):
    JWT_ALG: str = "HS256"
    JWT_SECRET: str = "abcxyz"
    JWT_EXP: int = 30  # minutes

    # REFRESH_TOKEN_KEY: str
    # REFRESH_TOKEN_EXP: timedelta = timedelta(days=30)

    SECURE_COOKIES: bool = True


auth_settings = AuthConfig()


# src.config
from pydantic_settings import BaseSettings

from app.constants import Environment


class Config(BaseSettings):
    MONGODB_URL: str = Environment.MONGO_HOST

    SITE_DOMAIN: str = "myapp.com"

    # ENVIRONMENT: Environment = Environment.PRODUCTION

    SENTRY_DSN: str | None = None

    CORS_ORIGINS: list[str]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS: list[str]

    APP_VERSION: str = "1.0"


settings = Config()
