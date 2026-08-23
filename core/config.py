from functools import lru_cache

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env",
                              extra="ignore")

    DATABASE_URL: str = "sqlite:///./sql_app.db"
    FIELD_ENCRYPTION_KEY: str
    BLIND_INDEX_KEY: str

# Returns an instance of settings for access to the env settings.
@lru_cache
def get_settings():
    return Settings()