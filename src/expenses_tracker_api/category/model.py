from datetime import datetime
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from expenses_tracker_api.core.database import Base
from expenses_tracker_api.user.model import User


class Category(Base):
    __tablename__ = "categories"
    __table_args__ = {"schema": "public"}

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("public.users.id", onupdate="CASCADE", ondelete="CASCADE")
    )
    name: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(server_default="NOW()")

    user: Mapped[User | None] = relationship()
