from fastapi import FastAPI

from expenses_tracker_api.api.router import api_router
from expenses_tracker_api.core.exception_handlers import register_exception_handlers

app = FastAPI(title="Expenses Tracker API", version="0.1.0")

register_exception_handlers(app)

app.include_router(api_router)
