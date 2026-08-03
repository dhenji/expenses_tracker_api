from uuid import UUID

from expenses_tracker_api.shared.exceptions import DomainError


class ExpenseError(DomainError):
    """Base exception for expense-related errors."""

    pass


class ExpenseNotFoundError(ExpenseError):
    """Raised when a expense is not found by unique identifiers."""

    def __init__(self, *, id: UUID | None = None) -> None:
        if id is not None:
            super().__init__(f"Category with id {id} not found.")
        else:
            super().__init__("Category not found.")
