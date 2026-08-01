class ApplicationError(Exception):
    """Base exception for expected application errors."""


class DomainError(ApplicationError):
    """Base exception for domain-related errors."""


class DatabaseError(ApplicationError):
    """Base exception for database-related errors."""


class QueryError(DatabaseError):
    """Raised when querying data fails."""


class PersistenceError(DatabaseError):
    """Raised when an error occurs while persisting data to the database."""


class UniqueViolationError(DatabaseError):
    """Raised when a unique constraint is violated."""

    def __init__(self, constraint_name: str | None = None) -> None:
        self.constraint_name = constraint_name
        super().__init__("A unique constraint was violated.")


class ForeignKeyViolationError(DatabaseError):
    """Raised when a foreign key constraint is violated."""

    def __init__(self, constraint_name: str | None = None) -> None:
        self.constraint_name = constraint_name
        super().__init__("A foreign key constraint was violated.")
