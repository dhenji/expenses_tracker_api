from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from expenses_tracker_api.shared.exceptions import (
    ApplicationError,
    PersistenceError,
    QueryError,
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
    return PersistenceError(
        "A database constraint was violated.",
    )
