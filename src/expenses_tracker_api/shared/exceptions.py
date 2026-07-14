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
