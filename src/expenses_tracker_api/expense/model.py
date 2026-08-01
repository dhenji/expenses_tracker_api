from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

from sqlalchemy import Date, DateTime, ForeignKey, Numeric, String, func, text
from sqlalchemy.orm import Mapped, mapped_column

from expenses_tracker_api.core.database import Base


class Expense(Base):
    __tablename__ = "expenses"
    __table_args__ = {"schema": "public"}

    id: Mapped[UUID] = mapped_column(
        primary_key=True, server_default=text("gen_random_uuid()")
    )
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("public.users.id", onupdate="CASCADE", ondelete="RESTRICT")
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey("public.categories.id", onupdate="CASCADE", ondelete="RESTRICT")
    )
    amount: Mapped[Decimal] = mapped_column(Numeric, server_default="0")
    currency: Mapped[str] = mapped_column(String(3))
    description: Mapped[str] | None = mapped_column(String(255))
    expense_date: Mapped[date] = mapped_column(Date, server_default="CURRENT_DATE")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
