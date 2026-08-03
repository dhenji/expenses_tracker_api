from collections.abc import Callable, Sequence
from uuid import UUID

import expenses_tracker_api
from expenses_tracker_api.category.exceptions import CategoryNotFoundError
from expenses_tracker_api.category.model import Category
from expenses_tracker_api.core.unit_of_work import UnitOfWork
from expenses_tracker_api.expense.dto import CreateExpenseInput
from expenses_tracker_api.expense.exceptions import ExpenseNotFoundError
from expenses_tracker_api.expense.model import Expense
from expenses_tracker_api.expense.repository import ExpenseRepository
from expenses_tracker_api.user.exceptions import UserNotFoundError
from expenses_tracker_api.user.model import User


class ExpenseCommandService:
    def __init__(self, uow_factory: Callable[[], UnitOfWork]) -> None:
        self._uow_factory = uow_factory

    def create_expense(self, data: CreateExpenseInput, *, user_id: UUID) -> Expense:
        with self._uow_factory() as uow:
            user: User | None = uow.user_repo.get(user_id)

            if user is None:
                raise UserNotFoundError(id=user_id)

            category_id: int = data.category_id
            category: Category | None = uow.category_repo.get(category_id)

            if category is None:
                raise CategoryNotFoundError(id=category_id)

            expense = Expense(
                user_id=user_id,
                category_id=category_id,
                amount=data.amount,
                currency=data.currency,
                description=data.description,
            )

            if data.expense_date is not None:
                expense.expense_date = data.expense_date

            return uow.expense_repo.save(expense)

    def delete_expense(self, id: UUID) -> None:
        with self._uow_factory() as uow:
            expense: Expense | None = uow.expense_repo.get(id)

            if expense is None:
                raise ExpenseNotFoundError(id=id)

            uow.expense_repo.delete(expense)


class ExpenseQueryService:
    def __init__(self, query_repo: ExpenseRepository) -> None:
        self._query_repo = query_repo

    def get_all_expenses(self) -> Sequence[Expense]:
        return self._query_repo.get_all()

    def get_expense(self, id: UUID) -> Expense:
        expense: Expense | None = self._query_repo.get(id)

        if expense is None:
            raise ExpenseNotFoundError(id=id)

        return expense
