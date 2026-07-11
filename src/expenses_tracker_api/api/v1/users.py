from fastapi import APIRouter

router = APIRouter()


@router.get("/", summary="List users")
async def list_users():
    return []


@router.get("/{user_id}", summary="Get a user")
async def get_user(user_id: int):
    return {"id": user_id}
