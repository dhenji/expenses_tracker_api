class UserError(Exception):
    """Base exception for user-related errors."""


class EmailAlreadyExistsError(UserError):
    """Raised when a user email already exists."""
