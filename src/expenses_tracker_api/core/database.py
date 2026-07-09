from typing import Generator

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class Base(DeclarativeBase):
    pass


class Database:
    def __init__(self, url: str) -> None:
        self._engine: Engine = create_engine(url, pool_pre_ping=True)

        self._SessionLocal = sessionmaker(
            bind=self._engine, autoflush=False, class_=Session, expire_on_commit=False
        )

    def get_db(self) -> Generator[Session, None, None]:
        db = self._SessionLocal()
        try:
            yield db
        finally:
            db.close()
