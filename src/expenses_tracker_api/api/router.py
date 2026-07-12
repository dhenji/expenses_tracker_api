from fastapi import APIRouter

from expenses_tracker_api.api.v1.router import router as v1_router

api_router = APIRouter()

api_router.include_router(v1_router, prefix="/api/v1")
