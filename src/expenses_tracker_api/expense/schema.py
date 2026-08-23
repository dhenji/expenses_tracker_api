from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ExpenseBase(BaseModel):
    amount: Decimal
    currency: str
    description: str | None = None


class ExpenseCreate(ExpenseBase):
    user_id: UUID
    category_id: int
    expense_date: date | None = None


class ExpenseUpdate(BaseModel):
    category_id: int | None = None
    amount: Decimal | None = None
    currency: str | None = None
    description: str | None = None
    expense_date: date | None = None


class ExpenseResponse(ExpenseBase):
    id: UUID
    user_id: UUID
    category_id: int
    expense_date: date
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
