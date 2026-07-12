from fastapi import APIRouter

from expenses_tracker_api.api.v1.users import router as user_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["Users"])
