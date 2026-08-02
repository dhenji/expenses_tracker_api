from collections.abc import Awaitable, Callable

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from expenses_tracker_api.category.exceptions import (
    CategoryNameAlreadyExistsError,
    CategoryNotFoundError,
)
from expenses_tracker_api.shared.exceptions import (
    ApplicationError,
    DatabaseError,
    ForeignKeyViolationError,
    UniqueViolationError,
)
from expenses_tracker_api.user.exceptions import (
    EmailAlreadyExistsError,
    UserNotFoundError,
)

ExceptionHandler = Callable[..., Awaitable[JSONResponse]]


async def _application_error_handler(
    request: Request,
    exc: ApplicationError,
) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Application error.",
        },
    )


async def _database_error_handler(
    request: Request,
    exc: DatabaseError,
) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error.",
        },
    )


async def _unique_violation_error_handler(
    request: Request, exc: UniqueViolationError
) -> JSONResponse:
    messages = {
        "categories_name_key": "Category with this name already exists.",
    }
    return JSONResponse(
        status_code=409,
        content={
            "detail": messages.get(
                exc.constraint_name or "", "A unique constraint was violated."
            )
        },
    )


async def _foreign_key_violation_error_handler(
    request: Request, exc: ForeignKeyViolationError
) -> JSONResponse:
    messages = {
        "expenses_category_id_fkey": "Category is in use by expenses.",
    }
    return JSONResponse(
        status_code=409,
        content={
            "detail": messages.get(
                exc.constraint_name or "", "A foreign key constraint was violated."
            )
        },
    )


async def _email_already_exists_error_handler(
    request: Request, exc: EmailAlreadyExistsError
) -> JSONResponse:
    return JSONResponse(status_code=409, content={"detail": str(exc)})


async def _user_not_found_error_handler(
    request: Request, exc: UserNotFoundError
) -> JSONResponse:
    return JSONResponse(status_code=404, content={"detail": str(exc)})


async def _category_name_already_exists_error_handler(
    request: Request, exc: CategoryNameAlreadyExistsError
) -> JSONResponse:
    return JSONResponse(status_code=409, content={"detail": str(exc)})


async def _category_not_found_error_handler(
    request: Request, exc: CategoryNotFoundError
) -> JSONResponse:
    return JSONResponse(status_code=404, content={"detail": str(exc)})


def register_exception_handlers(app: FastAPI) -> None:
    handlers: dict[type[ApplicationError], ExceptionHandler] = {
        DatabaseError: _database_error_handler,
        ApplicationError: _application_error_handler,
        UniqueViolationError: _unique_violation_error_handler,
        ForeignKeyViolationError: _foreign_key_violation_error_handler,
        EmailAlreadyExistsError: _email_already_exists_error_handler,
        UserNotFoundError: _user_not_found_error_handler,
        CategoryNameAlreadyExistsError: _category_name_already_exists_error_handler,
        CategoryNotFoundError: _category_not_found_error_handler,
    }

    for exception, handler in handlers.items():
        app.add_exception_handler(exception, handler)
