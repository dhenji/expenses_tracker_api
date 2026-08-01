from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, String, func, text
from sqlalchemy.orm import Mapped, mapped_column

from expenses_tracker_api.core.database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "public"}

    id: Mapped[UUID] = mapped_column(
        primary_key=True, server_default=text("gen_random_uuid()")
    )

    first_name: Mapped[str] = mapped_column(String(50))

    last_name: Mapped[str] = mapped_column(String(50))

    email: Mapped[str] = mapped_column(String(254), unique=True)

    password_hash: Mapped[str] = mapped_column(String(255))

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
