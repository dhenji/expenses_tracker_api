from expenses_tracker_api.core.security import hash_password
from expenses_tracker_api.user.model import User
from expenses_tracker_api.user.repository import UserRepository
from expenses_tracker_api.user.schema import UserCreate, UserResponse


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def create_user(self, data: UserCreate) -> UserResponse:
        password_hash: str = hash_password(data.password)

        user = User(
            first_name=data.first_name,
            last_name=data.last_name,
            email=data.email,
            password_hash=password_hash,
        )

        saved_user: User = self.repository.save(user)

        return UserResponse.model_validate(saved_user)
