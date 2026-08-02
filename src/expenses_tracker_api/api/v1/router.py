from fastapi import APIRouter

from expenses_tracker_api.api.v1.categories import router as category_router
from expenses_tracker_api.api.v1.expenses import router as expense_router
from expenses_tracker_api.api.v1.users import router as user_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["Users"])
router.include_router(category_router, prefix="/categories", tags=["Categories"])
router.include_router(expense_router, prefix="/expenses", tags=["Expenses"])
