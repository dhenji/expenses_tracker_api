from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from expenses_tracker_api.core.database import database
from expenses_tracker_api.user.repository import UserRepository
from expenses_tracker_api.user.service import UserService


def get_db() -> Generator[Session, None, None]:
    yield from database.get_db()


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repository = UserRepository(db)

    return UserService(repository)
