from fastapi import FastAPI

from expenses_tracker_api.api.router import api_router

app = FastAPI(title="Expenses Tracker API", version="0.1.0")

app.include_router(api_router)
