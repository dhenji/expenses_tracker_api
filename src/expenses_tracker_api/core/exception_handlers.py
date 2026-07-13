from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from expenses_tracker_api.shared.exceptions import PersistenceError
from expenses_tracker_api.user.exceptions import EmailAlreadyExistsError


async def _email_exists_handler(
    request: Request, exc: EmailAlreadyExistsError
) -> JSONResponse:
    return JSONResponse(status_code=409, content={"detail": str(exc)})


async def _persistence_error_handler(
    request: Request,
    exc: PersistenceError,
) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error.",
        },
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(EmailAlreadyExistsError, _email_exists_handler)

    app.add_exception_handler(PersistenceError, _persistence_error_handler)
