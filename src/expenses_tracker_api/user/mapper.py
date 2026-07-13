from sqlalchemy.exc import IntegrityError

from expenses_tracker_api.shared.exceptions import PersistenceError
from expenses_tracker_api.user.exceptions import EmailAlreadyExistsError


def map_user_integrity_error(integrity_error: IntegrityError) -> Exception:
    constraint_name = getattr(
        getattr(integrity_error.orig, "diag", None),
        "constraint_name",
        None,
    )

    if constraint_name == "uq_users_email":
        return EmailAlreadyExistsError("Email already exists.")

    return PersistenceError("Unable to persist user.", original=integrity_error)
