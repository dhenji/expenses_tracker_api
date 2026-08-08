import re
from functools import cached_property, lru_cache
from pathlib import Path
from typing import Any
from urllib.parse import quote_plus

from pydantic_settings import BaseSettings, SettingsConfigDict


class _Secrets:
    """
    This class is for reading secrets needed by this project.
    """

    def __init__(self, secret_path: Path) -> None:
        self._secret_path = secret_path

    def read(self, secret_name: str) -> str | None:
        secret_path: Path = self._secret_path / secret_name

        if secret_path.exists():
            return secret_path.read_text().strip()

        return None


class Settings(BaseSettings):
    """
    This class is the configuration of this api project. Most of the Configuration are asign on .env file and mapped in this class using pydantic_settings package (library).

    The PG variables are configurations for connecting to PostgreSQL.
    """

    app_name: str
    environment: str
    debug: bool = False

    # PostgreSQL config
    db_pg_host: str
    db_pg_port: int
    db_pg_user: str
    db_pg_db_name: str
    db_pg_user_password: str | None = None

    # Docker secrets default path
    secrets_path: Path = Path("/run/secrets")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @cached_property
    def _secrets(self) -> _Secrets:
        return _Secrets(self.secrets_path)

    @property
    def db_pg_url(self) -> str:
        required: dict[str, str | int | None] = {
            "user": self.db_pg_user,
            "password": self.db_pg_user_password
            or self._secrets.read("pg_user_password"),
            "host": self.db_pg_host,
            "port": self.db_pg_port,
            "database_name": self.db_pg_db_name,
        }

        missing: list[str] = [key for key, value in required.items() if not value]

        if missing:
            raise ValueError(f"Missing PostgreSQL configuration: {', '.join(missing)}")

        return (
            "postgresql+psycopg://"
            f"{quote_plus(str(required['user']))}:"
            f"{quote_plus(str(required['password']))}@"
            f"{required['host']}:{required['port']}/"
            f"{required['database_name']}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
