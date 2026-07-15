from collections.abc import Generator

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from expenses_tracker_api.core.config import Settings, get_settings


class Base(DeclarativeBase):
    pass


class DatabaseSessionManager:
    def __init__(self, url: str) -> None:
        self._engine: Engine = create_engine(url, pool_pre_ping=True)

        self._session_factory = sessionmaker(
            bind=self._engine, autoflush=False, class_=Session, expire_on_commit=False
        )

    @property
    def engine(self) -> Engine:
        return self._engine

    def create_session(self) -> Session:
        return self._session_factory()


_settings: Settings = get_settings()
database = DatabaseSessionManager(_settings.db_pg_url)
