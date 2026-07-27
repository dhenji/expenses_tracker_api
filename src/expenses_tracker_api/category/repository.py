from collections.abc import Sequence
from uuid import UUID

from sqlalchemy import Select, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from expenses_tracker_api.category.model import Category
from expenses_tracker_api.shared.exceptions_mapper import (
    map_query_error,
    map_write_error,
)
from expenses_tracker_api.shared.repository_utils import (
    delete_entity,
    get_all_entities,
    get_entity,
    get_entity_by,
    save_entity,
)


class CategoryRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, category: Category) -> Category:
        return save_entity(self._session, category)

    def get_all(self) -> Sequence[Category]:
        return get_all_entities(self._session, Category)

    def get(self, id: int) -> Category | None:
        return get_entity(self._session, Category, id=id)

    def get_by_name(self, name: str) -> Category | None:
        return get_entity_by(self._session, Category, name=name)

    def delete(self, category: Category) -> None:
        return delete_entity(self._session, category)
