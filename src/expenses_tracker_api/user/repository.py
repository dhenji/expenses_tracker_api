from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from expenses_tracker_api.shared.exceptions import PersistenceError
from expenses_tracker_api.user.mapper import map_user_integrity_error
from expenses_tracker_api.user.model import User


class UserRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def save(self, user: User) -> User:
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)

            return user
        except IntegrityError as e:
            self.db.rollback()
            raise map_user_integrity_error(e) from e
        except SQLAlchemyError as e:
            self.db.rollback()
            raise PersistenceError("Database error while saving user.") from e
