from dataclasses import dataclass


@dataclass
class CreateCategoryInput:
    name: str
    description: str | None = None


@dataclass
class UpdateCategoryInput:
    name: str | None = None
    description: str | None = None
