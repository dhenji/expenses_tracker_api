from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from expenses_tracker_api.shared.exceptions import (
    ApplicationError,
    ForeignKeyViolationError,
    PersistenceError,
    QueryError,
    UniqueViolationError,
)


def map_write_error(error: SQLAlchemyError) -> ApplicationError:
    if isinstance(error, IntegrityError):
        return _map_integrity_error(error)

    return PersistenceError(
        "Unable to persist data.",
    )


def map_query_error(error: SQLAlchemyError) -> ApplicationError:
    return QueryError(
        "Unable to query data.",
    )


def _map_integrity_error(error: IntegrityError) -> ApplicationError:
    sqlstate = getattr(error.orig, "sqlstate", None)
    constraint_name = getattr(
        getattr(error.orig, "diag", None), "constraint_name", None
    )

    if sqlstate == "23505":  # unique_violation
        return UniqueViolationError(constraint_name)
    if sqlstate == "23503":  # foreign_key_violation
        return ForeignKeyViolationError(constraint_name)

    return PersistenceError("A database constraint was violated.")
