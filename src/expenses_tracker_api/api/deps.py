from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from expenses_tracker_api.category.repository import CategoryRepository
from expenses_tracker_api.category.service import (
    CategoryCommandService,
    CategoryQueryService,
)
from expenses_tracker_api.core.database import database
from expenses_tracker_api.core.unit_of_work import UnitOfWork
from expenses_tracker_api.expense.repository import ExpenseRepository
from expenses_tracker_api.expense.service import (
    ExpenseCommandService,
    ExpenseQueryService,
)
from expenses_tracker_api.user.repository import UserRepository
from expenses_tracker_api.user.service import UserCommandService, UserQueryService


def get_session() -> Generator[Session, None, None]:
    session = database.create_session()
    try:
        yield session
    finally:
        session.close()


def get_uow() -> UnitOfWork:
    return UnitOfWork(database.create_session())


def get_user_command_service() -> UserCommandService:
    return UserCommandService(
        uow_factory=get_uow,
    )


def get_user_query_service(
    session: Session = Depends(get_session),
) -> UserQueryService:
    query_repository = UserRepository(session)

    return UserQueryService(query_repository)


def get_category_command_service() -> CategoryCommandService:
    return CategoryCommandService(uow_factory=get_uow)


def get_category_query_service(
    session: Session = Depends(get_session),
) -> CategoryQueryService:
    query_repository = CategoryRepository(session)
    return CategoryQueryService(query_repository)


def get_expense_command_service() -> ExpenseCommandService:
    return ExpenseCommandService(uow_factory=get_uow)


def get_expense_query_service(
    session: Session = Depends(get_session),
) -> ExpenseQueryService:
    query_repository = ExpenseRepository(session)

    return ExpenseQueryService(query_repository)
