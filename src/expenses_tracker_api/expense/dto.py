from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class CreateExpenseInput:
    category_id: int
    amount: Decimal
    currency: str
    description: str | None = None
    expense_date: date | None = None
