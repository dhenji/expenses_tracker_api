from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CategoryBase(BaseModel):
    name: str
    description: str | None = None


class CategoryCreate(CategoryBase):
    user_id: UUID


class CategoryResponse(CategoryBase):
    id: int
    user_id: UUID | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
