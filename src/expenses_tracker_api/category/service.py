from collections.abc import Callable
from uuid import UUID

from expenses_tracker_api.category.dto import CreateCategoryInput
from expenses_tracker_api.category.exceptions import CategoryNameAlreadyExistsError
from expenses_tracker_api.category.model import Category
from expenses_tracker_api.core.unit_of_work import UnitOfWork
from expenses_tracker_api.user.exceptions import UserNotFoundError
from expenses_tracker_api.user.model import User


class CategoryCommandService:
    def __init__(self, uow_factory: Callable[[], UnitOfWork]) -> None:
        self._uow_factory = uow_factory

    def create_category(
        self, data: CreateCategoryInput, *, user_id: UUID | None = None
    ) -> Category:
        with self._uow_factory() as uow:
            if user_id:
                user: User | None = uow.user_repo.get(user_id)

                if not user:
                    raise UserNotFoundError(id=user_id)

            existing: Category | None = uow.category_repo.get_by_name(data.name)

            if existing:
                raise CategoryNameAlreadyExistsError(data.name)

            category = Category(
                user_id=user_id,
                name=data.name,
                description=data.description,
            )

            return uow.category_repo.save(category)
