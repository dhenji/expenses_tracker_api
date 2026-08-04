from collections.abc import Sequence
from uuid import UUID

from fastapi import APIRouter, Depends, status
from starlette.status import HTTP_200_OK

from expenses_tracker_api.api.deps import (
    get_expense_command_service,
    get_expense_query_service,
)
from expenses_tracker_api.expense.dto import CreateExpenseInput
from expenses_tracker_api.expense.model import Expense
from expenses_tracker_api.expense.schema import ExpenseCreate, ExpenseResponse
from expenses_tracker_api.expense.service import (
    ExpenseCommandService,
    ExpenseQueryService,
)

router = APIRouter()


@router.post(
    "/",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a expense",
)
def create_expense(
    expense_data: ExpenseCreate,
    service: ExpenseCommandService = Depends(get_expense_command_service),
) -> ExpenseResponse:
    expense: Expense = service.create_expense(
        CreateExpenseInput(
            category_id=expense_data.category_id,
            amount=expense_data.amount,
            currency=expense_data.currency,
            description=expense_data.description,
            expense_date=expense_data.expense_date,
        ),
        user_id=expense_data.user_id,
    )

    return ExpenseResponse.model_validate(expense)


@router.get(
    "/",
    response_model=list[ExpenseResponse],
    status_code=status.HTTP_200_OK,
    summary="Get all expenses",
)
def get_all_expenses(
    service: ExpenseQueryService = Depends(get_expense_query_service),
) -> list[ExpenseResponse]:
    expenses: Sequence = service.get_all_expenses()

    return [ExpenseResponse.model_validate(expense) for expense in expenses]


@router.get(
    "/{expense_id}",
    response_model=ExpenseResponse,
    status_code=status.HTTP_200_OK,
    summary="Get expense using id",
)
def get_expense(
    expense_id: UUID,
    service: ExpenseQueryService = Depends(get_expense_query_service),
) -> ExpenseResponse:
    return ExpenseResponse.model_validate(service.get_expense(expense_id))
