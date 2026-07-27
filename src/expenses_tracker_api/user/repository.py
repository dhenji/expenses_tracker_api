from collections.abc import Sequence
from uuid import UUID

from sqlalchemy.orm import Session

from expenses_tracker_api.shared.repository_utils import (
    delete_entity,
    get_all_entities,
    get_entity,
    get_entity_by,
    save_entity,
)
from expenses_tracker_api.user.model import User


class UserRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, user: User) -> User:
        return save_entity(self._session, user)

    def get(self, id: UUID) -> User | None:
        return get_entity(self._session, User, id=id)

    def get_all(self) -> Sequence[User]:
        return get_all_entities(self._session, User)

    def get_by_email(self, email: str) -> User | None:
        return get_entity_by(self._session, User, email=email)

    def delete(self, user: User) -> None:
        delete_entity(self._session, user)
