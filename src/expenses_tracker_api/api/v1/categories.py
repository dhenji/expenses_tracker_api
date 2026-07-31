from typing import Sequence

from fastapi import APIRouter, Depends, status

from expenses_tracker_api.api.deps import (
    get_category_command_service,
    get_category_query_service,
)
from expenses_tracker_api.category.dto import CreateCategoryInput
from expenses_tracker_api.category.model import Category
from expenses_tracker_api.category.schema import CategoryCreate, CategoryResponse
from expenses_tracker_api.category.service import (
    CategoryCommandService,
    CategoryQueryService,
)

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


@router.get(
    "/",
    response_model=list[CategoryResponse],
    status_code=status.HTTP_200_OK,
    summary="List categories",
)
def list_categories(
    service: CategoryQueryService = Depends(get_category_query_service),
) -> list[CategoryResponse]:
    categories: Sequence[Category] = service.get_all_categories()

    return [CategoryResponse.model_validate(category) for category in categories]


@router.get(
    "/by-name/{name}",
    response_model=CategoryResponse,
    status_code=status.HTTP_200_OK,
    summary="Get a category using name",
)
def get_category_by_name(
    name: str, service: CategoryQueryService = Depends(get_category_query_service)
) -> CategoryResponse:
    category: Category = service.get_category_by_name(name)

    return CategoryResponse.model_validate(category)
