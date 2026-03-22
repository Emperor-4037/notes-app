from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    DB_USER : str
    DB_PASS : str
    DB_HOST : Optional[str] = "127.0.0.1"
    DB_PORT : Optional[int] = 5432
    DB_NAME : str


    SECRET_KEY : str
    ALGORITHM : str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 60 * 24


    model_config = SettingsConfigDict(
        env_file = BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
        )


settings = Settings()