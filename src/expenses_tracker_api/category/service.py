from collections.abc import Callable
from typing import Sequence
from uuid import UUID

from expenses_tracker_api.category.dto import CreateCategoryInput, UpdateCategoryInput
from expenses_tracker_api.category.exceptions import (
    CategoryNameAlreadyExistsError,
    CategoryNotFoundError,
)
from expenses_tracker_api.category.model import Category
from expenses_tracker_api.category.repository import CategoryRepository
from expenses_tracker_api.core.unit_of_work import UnitOfWork
from expenses_tracker_api.user.exceptions import UserNotFoundError
from expenses_tracker_api.user.model import User


class CategoryCommandService:
    def __init__(self, uow_factory: Callable[[], UnitOfWork]) -> None:
        self._uow_factory = uow_factory

    def create_category(self, data: CreateCategoryInput, *, user_id: UUID) -> Category:
        with self._uow_factory() as uow:
            user: User | None = uow.user_repo.get(user_id)

            if user is None:
                raise UserNotFoundError(id=user_id)

            existing: Category | None = uow.category_repo.get_by_name(data.name)

            if existing is not None:
                raise CategoryNameAlreadyExistsError(data.name)

            category = Category(
                user_id=user_id,
                name=data.name,
                description=data.description,
            )

            return uow.category_repo.save(category)

    def update_category(
        self, data: UpdateCategoryInput, *, user_id: UUID, category_id: int
    ) -> Category:
        with self._uow_factory() as uow:
            user: User | None = uow.user_repo.get(user_id)

            if user is None:
                raise UserNotFoundError(id=user_id)

            category: Category | None = uow.category_repo.get(category_id)
            if category is None or category.user_id != user_id:
                raise CategoryNotFoundError(id=category_id)

            if data.name is not None:
                existing: Category | None = uow.category_repo.get_by_name(data.name)

                if existing is not None:
                    raise CategoryNameAlreadyExistsError(name=data.name)

                category.name = data.name

            if data.description is not None:
                category.description = data.description

            return category

    def delete_category(self, id: int) -> None:
        with self._uow_factory() as uow:
            category: Category | None = uow.category_repo.get(id)

            if category is None:
                raise CategoryNotFoundError(id=id)

            uow.category_repo.delete(category)


class CategoryQueryService:
    def __init__(self, query_repo: CategoryRepository) -> None:
        self._query_repo = query_repo

    def get_all_categories(self) -> Sequence[Category]:
        return self._query_repo.get_all()

    def get_category(self, id: int) -> Category:
        category: Category | None = self._query_repo.get(id)

        if category is None:
            raise CategoryNotFoundError(id=id)

        return category

    def get_category_by_name(self, name: str) -> Category:
        category: Category | None = self._query_repo.get_by_name(name)

        if category is None:
            raise CategoryNotFoundError(name=name)

        return category
