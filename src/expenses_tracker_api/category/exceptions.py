from expenses_tracker_api.shared.exceptions import DomainError


class CategoryError(DomainError):
    """Base exception for category-related errors."""

    pass


class CategoryNotFoundError(CategoryError):
    """Raised when a category is not found by unique identifiers."""

    def __init__(self, *, id: int | None = None, name: str | None = None) -> None:
        if id is not None:
            super().__init__(f"Category with id {id} not found.")
        elif name is not None:
            super().__init__(f"Category with name '{name}' not found.")
        else:
            super().__init__("Category not found.")


class CategoryNameAlreadyExistsError(CategoryError):
    """Raised when a category name already exists."""

    def __init__(self, name: str) -> None:
        super().__init__(f"Category with name '{name}' already exists.")
