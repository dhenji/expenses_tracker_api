from typing import Sequence
from uuid import UUID

from sqlalchemy import Select, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from expenses_tracker_api.shared.exceptions_mapper import (
    map_query_error,
    map_write_error,
)
from expenses_tracker_api.user.model import User


class UserRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, user: User) -> User:
        try:
            self._session.add(user)
            self._session.refresh(user)

            return user
        except SQLAlchemyError as e:
            raise map_write_error(e) from e

    def get_all(self) -> Sequence[User]:
        try:
            stmt: Select[tuple[User]] = select(User)
            return self._session.scalars(stmt).all()
        except SQLAlchemyError as e:
            raise map_query_error(e) from e

    def get_by_email(self, email: str) -> User | None:
        try:
            stmt: Select[tuple[User]] = select(User).where(User.email == email)
            return self._session.execute(stmt).scalar_one_or_none()
        except SQLAlchemyError as e:
            raise map_query_error(e) from e

    def get_by_id(self, id: UUID) -> User | None:
        try:
            return self._session.get(User, id)
        except SQLAlchemyError as e:
            raise map_query_error(e) from e
