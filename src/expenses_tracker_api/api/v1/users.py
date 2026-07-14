from fastapi import APIRouter, Depends, status

from expenses_tracker_api.api.deps import get_user_service
from expenses_tracker_api.user.schema import UserCreate, UserResponse
from expenses_tracker_api.user.service import UserService

router = APIRouter()


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a user",
)
def create_user(
    user_data: UserCreate,
    service: UserService = Depends(get_user_service),
) -> UserResponse:
    return service.create_user(user_data)


@router.get(
    "/",
    response_model=list[UserResponse],
    summary="List users",
    status_code=status.HTTP_200_OK,
)
async def list_users(
    service: UserService = Depends(get_user_service),
) -> list[UserResponse]:
    return service.get_all_users()


@router.get(
    "/{user_email}",
    response_model=UserResponse,
    summary="Get a user using email",
    status_code=status.HTTP_200_OK,
)
async def get_user_by_email() -> UserResponse:
    return {"id": user_id}
