from fastapi import APIRouter, Depends, status

from expenses_tracker_api.api.deps import get_category_command_service
from expenses_tracker_api.category.dto import CreateCategoryInput
from expenses_tracker_api.category.model import Category
from expenses_tracker_api.category.schema import CategoryCreate, CategoryResponse
from expenses_tracker_api.category.service import CategoryCommandService

router = APIRouter()


@router.post(
    "/",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a category",
)
def create_category(
    category_data: CategoryCreate,
    service: CategoryCommandService = Depends(get_category_command_service),
) -> CategoryResponse:
    category: Category = service.create_category(
        CreateCategoryInput(
            name=category_data.name, description=category_data.description
        ),
        user_id=None,
    )

    return CategoryResponse.model_validate(category)
