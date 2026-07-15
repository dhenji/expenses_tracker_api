from expenses_tracker_api.shared.exceptions import DomainError


class UserError(DomainError):
    """Base exception for user-related errors."""


class EmailAlreadyExistsError(UserError):
    """Raised when a user email already exists."""


class UserNotFoundError(UserError):
    """Raised when a user is not found by unique identifiers."""
