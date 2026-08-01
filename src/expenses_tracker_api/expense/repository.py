from collections.abc import Sequence
from uuid import UUID

from sqlalchemy.orm import Session

from expenses_tracker_api.expense.model import Expense
from expenses_tracker_api.shared.repository_utils import (
    delete_entity,
    get_all_entities,
    get_entity,
    save_entity,
)


class ExpenseRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, expense: Expense) -> Expense:
        return save_entity(self._session, expense)

    def get_all(self) -> Sequence[Expense]:
        return get_all_entities(self._session, Expense)

    def get(self, id: UUID) -> Expense | None:
        return get_entity(self._session, Expense, id=id)

    def delete(self, expense: Expense) -> None:
        return delete_entity(self._session, expense)
