from fastapi import APIRouter, Depends, status

from expenses_tracker_api.expense.dto import CreateExpenseInput
from expenses_tracker_api.expense.model import Expense
from expenses_tracker_api.expense.schema import ExpenseCreate, ExpenseResponse
from expenses_tracker_api.expense.service import ExpenseCommandService

router = APIRouter()


@router.post(
    "/",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a expense",
)
def create_expense(
    expense_data: ExpenseCreate, service: ExpenseCommandService = Depends()
) -> ExpenseResponse:
    expense: Expense = service.create_expense(
        CreateExpenseInput(
            category_id=expense_data.category_id,
            amount=expense_data.amount,
            currency=expense_data.currency,
            description=expense_data.description,
            expense_date=expense_data.expense_date,
        )
    )
