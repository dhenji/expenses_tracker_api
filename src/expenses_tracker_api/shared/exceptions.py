class DatabaseError(Exception):
    """Base error for database-related error"""


class PersistenceError(DatabaseError):
    """Raised when an error occurs while persisting data to the database."""

    def __init__(self, message: str, original: Exception | None = None) -> None:
        super().__init__(message)
        self.original = original
