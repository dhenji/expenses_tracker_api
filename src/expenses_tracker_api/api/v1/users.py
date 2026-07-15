from typing import Sequence

from fastapi import APIRouter, Depends, status
from pydantic import EmailStr

from expenses_tracker_api.api.deps import (
    get_user_command_service,
    get_user_query_service,
)
from expenses_tracker_api.user.dto import CreateUserInput
from expenses_tracker_api.user.model import User
from expenses_tracker_api.user.schema import UserCreate, UserResponse
from expenses_tracker_api.user.service import UserCommandService, UserQueryService

router = APIRouter()


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a user",
)
def create_user(
    user_data: UserCreate,
    service: UserCommandService = Depends(get_user_command_service),
) -> UserResponse:
    user: User = service.create_user(
        CreateUserInput(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            password=user_data.password,
        )
    )

    return UserResponse.model_validate(user)


@router.get(
    "/",
    response_model=list[UserResponse],
    summary="List users",
    status_code=status.HTTP_200_OK,
)
def list_users(
    service: UserQueryService = Depends(get_user_query_service),
) -> list[UserResponse]:
    users: Sequence[User] = service.get_all_users()

    return [UserResponse.model_validate(user) for user in users]


@router.get(
    "/by-email/{email}",
    response_model=UserResponse,
    summary="Get a user using email",
    status_code=status.HTTP_200_OK,
)
def get_user_by_email(
    email: EmailStr,
    service: UserQueryService = Depends(get_user_query_service),
) -> UserResponse:
    user: User = service.get_user_by_email(str(email))

    return UserResponse.model_validate(user)
