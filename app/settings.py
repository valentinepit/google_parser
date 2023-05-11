from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv(verbose=True)


class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_port: int
    db_host: str

    class Config:
        env_file = "../.env"
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
