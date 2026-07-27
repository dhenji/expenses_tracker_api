from uuid import UUID

from expenses_tracker_api.shared.exceptions import DomainError


class UserError(DomainError):
    """Base exception for user-related errors."""


class EmailAlreadyExistsError(UserError):
    """Raised when a user email already exists."""

    def __init__(self, email: str) -> None:
        super().__init__(f"User with email '{email}' already exists.")


class UserNotFoundError(UserError):
    """Raised when a user is not found by unique identifiers."""

    def __init__(self, *, id: UUID | None = None, email: str | None = None) -> None:
        if id is not None:
            super().__init__(f"User with id {id} not found.")
        elif email is not None:
            super().__init__(f"User with email '{email}' not found.")
        else:
            super().__init__(f"User not found.")
