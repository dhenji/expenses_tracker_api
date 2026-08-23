from typing import Sequence
from uuid import UUID

from fastapi import APIRouter, Depends, status

from expenses_tracker_api.api.deps import (
    get_category_command_service,
    get_category_query_service,
)
from expenses_tracker_api.category.dto import CreateCategoryInput, UpdateCategoryInput
from expenses_tracker_api.category.model import Category
from expenses_tracker_api.category.schema import (
    CategoryCreate,
    CategoryResponse,
    CategoryUpdate,
)
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
        user_id=category_data.user_id,
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
    "/{category_id}",
    response_model=CategoryResponse,
    status_code=status.HTTP_200_OK,
    summary="Get a category using id",
)
def get_category(
    category_id: int,
    service: CategoryQueryService = Depends(get_category_query_service),
) -> CategoryResponse:
    category: Category = service.get_category(category_id)

    return CategoryResponse.model_validate(category)


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


@router.patch(
    "/{user_id}/{category_id}",
    response_model=CategoryResponse,
    status_code=status.HTTP_200_OK,
    summary="Update a category using user_id and category_id",
)
def update_category(
    user_id: UUID,
    category_id: int,
    category_data: CategoryUpdate,
    service: CategoryCommandService = Depends(get_category_command_service),
) -> CategoryResponse:
    category: Category = service.update_category(
        UpdateCategoryInput(
            name=category_data.name, description=category_data.description
        ),
        user_id=user_id,
        category_id=category_id,
    )

    return CategoryResponse.model_validate(category)


@router.delete(
    "/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete category using id",
)
def delete_category(
    category_id: int,
    service: CategoryCommandService = Depends(get_category_command_service),
) -> None:
    service.delete_category(category_id)
