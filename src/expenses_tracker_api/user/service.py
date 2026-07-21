from collections.abc import Callable
from typing import Sequence
from uuid import UUID

from expenses_tracker_api.core.security import hash_password
from expenses_tracker_api.core.unit_of_work import UnitOfWork
from expenses_tracker_api.user.dto import CreateUserInput, UpdateUserInput
from expenses_tracker_api.user.exceptions import (
    EmailAlreadyExistsError,
    UserNotFoundError,
)
from expenses_tracker_api.user.model import User
from expenses_tracker_api.user.repository import UserRepository


class UserCommandService:
    def __init__(self, uow_factory: Callable[[], UnitOfWork]) -> None:
        self._uow_factory = uow_factory

    def create_user(self, data: CreateUserInput) -> User:
        with self._uow_factory() as uow:
            email: str = data.email
            existing: User | None = uow.user_repo.get_by_email(email)

            if existing:
                raise EmailAlreadyExistsError(
                    f"User with an email of {email} already exists."
                )

            password_hash: str = hash_password(data.password)

            user = User(
                first_name=data.first_name,
                last_name=data.last_name,
                email=email,
                password_hash=password_hash,
            )

            return uow.user_repo.save(user)

    def update_user(self, id: UUID, data: UpdateUserInput) -> User:
        with self._uow_factory() as uow:
            user: User | None = uow.user_repo.get_by_id(id)

            if user is None:
                raise UserNotFoundError(f"User with an id of {id} doesn't exists.")

            if data.email is not None and data.email != user.email:
                existing: User | None = uow.user_repo.get_by_email(data.email)

                if existing:
                    raise EmailAlreadyExistsError(
                        f"User with an email of {data.email} already exists."
                    )

                user.email = data.email

            if data.first_name is not None:
                user.first_name = data.first_name
            if data.last_name is not None:
                user.last_name = data.last_name
            if data.password is not None:
                user.password_hash = hash_password(data.password)

            return uow.user_repo.save(user)


class UserQueryService:
    def __init__(self, query_repo: UserRepository) -> None:
        self._query_repo = query_repo

    def get_all_users(self) -> Sequence[User]:
        return self._query_repo.get_all()

    def get_user_by_email(self, email: str) -> User:
        user = self._query_repo.get_by_email(email)

        if user is None:
            raise UserNotFoundError(f"User with an email of {email} doesn't exists.")

        return user
