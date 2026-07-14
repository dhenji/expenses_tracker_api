from types import TracebackType
from typing import Self

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from expenses_tracker_api.shared.exceptions_mapper import map_write_error
from expenses_tracker_api.user.repository import UserRepository


class UnitOfWork:
    def __init__(self, session: Session) -> None:
        self.session = session

        self.user_repo = UserRepository(session)

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        try:
            if exc_type:
                self.rollback()
            else:
                self.commit()
        finally:
            self.close()

    def commit(self) -> None:
        try:
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise map_write_error(e) from e

    def rollback(self) -> None:
        self.session.rollback()

    def close(self) -> None:
        self.session.close()
