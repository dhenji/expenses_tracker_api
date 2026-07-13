from fastapi import APIRouter, Depends, status

from expenses_tracker_api.api.deps import get_user_service
from expenses_tracker_api.user.schema import UserCreate, UserResponse
from expenses_tracker_api.user.service import UserService

router = APIRouter()


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_data: UserCreate,
    service: UserService = Depends(get_user_service),
) -> UserResponse:
    return service.create_user(user_data)


@router.get("/", summary="List users")
async def list_users():
    return []


@router.get("/{user_id}", summary="Get a user")
async def get_user(user_id: int):
    return {"id": user_id}
